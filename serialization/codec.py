from typing import Any, Generic, TypeVar, List, Dict
from abc import abstractmethod

T = TypeVar('T')


class Codec(Generic[T]):
    @abstractmethod
    def encode(self, value: T) -> bytes: ...

    @abstractmethod
    def decode(self, data: bytearray) -> T: ...

    @abstractmethod
    def type_check(self, value: Any) -> bool: ...


class NoneCodec(Codec[None]):
    def encode(self, value: None) -> bytes:
        return b''

    def decode(self, data: bytearray) -> None:
        return None

    def type_check(self, value: Any) -> bool:
        return value is None


class BoolCodec(Codec[bool]):
    def encode(self, value: bool) -> bytes:
        return bytes((int(value),))

    def decode(self, data: bytearray) -> bool:
        return bool(data.pop(0))

    def type_check(self, value: Any) -> bool:
        return isinstance(value, bool)


class IntCodec(Codec[int]):
    def encode(self, value: int) -> bytes:
        return bytes(self.int_to_bytes(value))

    def decode(self, data: bytearray) -> int:
        x = data.pop(0)
        has_next = bool(x & 0x80)
        negative = bool(x & 0x40)
        x = x & 0x3F
        result = x
        offset = 6

        while has_next:
            x = data.pop(0)
            has_next = bool(x & 0x80)
            x = x & 0x7F
            result = result | (x << offset)
            offset += 7

        if negative:
            return -result
        else:
            return result

    def type_check(self, value: Any) -> bool:
        return isinstance(value, int)

    def int_to_bytes(self, value: int):
        negative = False
        if value < 0:
            value = -value
            negative = True

        x = value & 0x3F
        value = value >> 6
        if negative:
            x = x | 0x40
        if value > 0:
            x = x | 0x80
        yield x

        while value != 0:
            x = value & 0x7F
            value = value >> 7
            if value != 0:
                x = x | 0x80
            yield x


class StrCodec(Codec[str]):
    def encode(self, value: str) -> bytes:
        data = value.encode()
        return IntCodec().encode(len(data)) + data

    def decode(self, data: bytearray) -> str:
        length = IntCodec().decode(data)
        result = data[:length].decode()
        del data[:length]
        return result

    def type_check(self, value: Any) -> bool:
        return isinstance(value, str)


class FloatCodec(Codec[float]):
    def encode(self, value: T) -> bytes:
        from struct import pack
        return pack('>f', value)

    def decode(self, data: bytearray) -> T:
        from struct import unpack
        result, = unpack('>f', data[:4])
        del data[:4]
        return result

    def type_check(self, value: Any) -> bool:
        return isinstance(value, float)


codecs: List[Codec] = [
    NoneCodec(),
    BoolCodec(),
    IntCodec(),
    FloatCodec(),
    StrCodec()
]
cache: Dict[type, Codec] = {}


def dumps(obj: Any) -> bytes:
    tp = type(obj)
    if tp not in cache:
        for codec in codecs:
            if codec.type_check(obj):
                cache[tp] = codec
    codec = cache[tp]
    return codec.encode(obj)


def loads(data: bytes) -> Any:
    pass


print(loads(dumps(123)))
print(loads(dumps(True)))
print(loads(dumps('123')))
print(loads(dumps(123.45)))
