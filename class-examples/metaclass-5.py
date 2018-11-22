from typing import Any, Optional, Union, Type, Callable, List, Dict, BinaryIO

from io import BytesIO
from uuid import UUID, uuid5
from struct import pack, unpack
from collections import OrderedDict


Resolver = Callable[[Any], Optional[Type['Serializer']]]


def create_uid(name: str) -> int:
    src = uuid5(UUID('c0dec0de-1234-5678-9abc-5e21a113ab1e'), name).bytes
    uid = 0
    for i in range(4):
        for j in range(4):
            uid = uid ^ (src[4 * i + j] << 8 * j)
    return uid


class SerializerMeta(type):
    _uid_map: Dict[int, Type['Serializer']] = {}
    _type_map: Dict[type, Type['Serializer']] = {}
    _resolvers: List[Resolver] = []

    def __new__(mcs, name, bases, namespace, hint: Union[None, Type, Resolver] = None):
        uid = create_uid(name)

        cls: Type['Serializer'] = type.__new__(mcs, name, bases, namespace)
        cls.uid = uid

        mcs._uid_map[uid] = cls
        if hint is not None:
            if isinstance(hint, type):
                mcs._type_map[hint] = cls
            else:
                mcs._resolvers.append(hint)

        return cls

    @classmethod
    def resolve_uid(mcs, uid: int) -> Type['Serializer']:
        if uid in mcs._uid_map:
            return mcs._uid_map[uid]
        raise ValueError('serializer not found for %d' % uid)

    @classmethod
    def resolve_type(mcs, value: Any) -> Type['Serializer']:
        for base in type(value).__mro__:
            if base in mcs._type_map:
                return mcs._type_map[base]
        for resolver in mcs._resolvers:
            cls = resolver(value)
            if cls is not None:
                return cls
        raise ValueError('serializer not found for %s' % type(value).__name__)


class Serializer(object, metaclass=SerializerMeta):
    @classmethod
    def convert(cls, value: Any) -> Any:
        raise NotImplementedError()

    @classmethod
    def dump(cls, value: Any, io: BinaryIO) -> None:
        if cls is not Serializer:
            raise NotImplementedError()
        serializer = SerializerMeta.resolve_type(value)
        io.write(pack('>I', serializer.uid))
        serializer.dump(value, io)

    @classmethod
    def load(cls, io: BinaryIO) -> Any:
        if cls is not Serializer:
            raise NotImplementedError()
        uid, = unpack('>I', io.read(4))
        serializer = SerializerMeta.resolve_uid(uid)
        return serializer.load(io)


class Integer(Serializer, hint=int):
    @classmethod
    def convert(cls, value: Any) -> int:
        assert isinstance(value, int)
        assert abs(value) < 0x40000000
        return value

    @classmethod
    def dump(cls, value: int, io: BinaryIO) -> None:
        if value < 0:
            value = -value
            sign = 1
        else:
            sign = 0

        if value < (1 << 6):
            data = bytearray(1)
            data[0] = 0b00000000 | (sign << 6)
            offset = 0
        elif value < (1 << 10):
            data = bytearray(2)
            data[0] = 0b11000000 | (sign << 4)
            offset = 6
        elif value < (1 << 15):
            data = bytearray(3)
            data[0] = 0b11100000 | (sign << 3)
            offset = 12
        elif value < (1 << 20):
            data = bytearray(4)
            data[0] = 0b11110000 | (sign << 2)
            offset = 18
        elif value < (1 << 25):
            data = bytearray(5)
            data[0] = 0b11111000 | (sign << 1)
            offset = 24
        elif value < (1 << 30):
            data = bytearray(6)
            data[0] = 0b11111100 | sign
            offset = 30
        else:
            raise ValueError('value is out of range')

        data[0] |= value >> offset
        for i in range(1, 1 + offset // 6):
            data[i] = 0x80 | (value >> (offset - 6 * i)) & 0x3F

        io.write(data)

    @classmethod
    def load(cls, io: BinaryIO) -> int:
        data = io.read(1)

        header = data[0]
        if (header & 0b11111110) == 0b11111100:
            sign = header & 0b00000001
            value = 0
            data += io.read(5)
        elif (header & 0b11111100) == 0b11111000:
            sign = header & 0b00000010
            value = header & 0b00000001
            data += io.read(4)
        elif (header & 0b11111000) == 0b11110000:
            sign = header & 0b00000100
            value = header & 0b00000011
            data += io.read(3)
        elif (header & 0b11110000) == 0b11100000:
            sign = header & 0b00001000
            value = header & 0b00000111
            data += io.read(2)
        elif (header & 0b11100000) == 0b11000000:
            sign = header & 0b00010000
            value = header & 0b00001111
            data += io.read(1)
        else:
            assert not (header & 0b10000000)
            sign = header & 0b01000000
            value = header & 0b00111111

        for i in range(1, len(data)):
            octet = data[i]
            assert (octet & 0xC0) == 0x80
            value = (value << 6) | (octet & 0x3F)

        if sign:
            value = -value
        return value


class UnsignedInteger(Serializer):
    @classmethod
    def convert(cls, value: Any) -> int:
        assert isinstance(value, int)
        assert 0 <= value < 0x80000000
        return value

    @classmethod
    def dump(cls, value: int, io: BinaryIO) -> None:
        assert value >= 0

        if value < (1 << 7):
            data = bytearray(1)
            offset = 0
        elif value < (1 << 11):
            data = bytearray(2)
            data[0] = 0b11000000
            offset = 6
        elif value < (1 << 16):
            data = bytearray(3)
            data[0] = 0b11100000
            offset = 12
        elif value < (1 << 21):
            data = bytearray(4)
            data[0] = 0b11110000
            offset = 18
        elif value < (1 << 26):
            data = bytearray(5)
            data[0] = 0b11111000
            offset = 24
        elif value < (1 << 31):
            data = bytearray(6)
            data[0] = 0b11111100
            offset = 30
        else:
            raise ValueError('value is out of range')

        data[0] |= value >> offset
        for i in range(1, 1 + offset // 6):
            data[i] = 0x80 | (value >> (offset - 6 * i)) & 0x3F

        io.write(data)

    @classmethod
    def load(cls, io: BinaryIO) -> int:
        data = io.read(1)

        header = data[0]
        if (header & 0b11111110) == 0b11111100:
            value = header & 0b00000001
            data += io.read(5)
        elif (header & 0b11111100) == 0b11111000:
            value = header & 0b00000011
            data += io.read(4)
        elif (header & 0b11111000) == 0b11110000:
            value = header & 0b00000111
            data += io.read(3)
        elif (header & 0b11110000) == 0b11100000:
            value = header & 0b00001111
            data += io.read(2)
        elif (header & 0b11100000) == 0b11000000:
            value = header & 0b00011111
            data += io.read(1)
        else:
            assert not (header & 0b10000000)
            value = header

        for i in range(1, len(data)):
            assert (data[i] & 0xC0) == 0x80
            value = (value << 6) | (data[i] & 0x3F)

        return value


class Float(Serializer, hint=float):
    @classmethod
    def convert(cls, value: Any) -> float:
        assert isinstance(value, (float, int))
        return float(value)

    @classmethod
    def dump(cls, value: float, io: BinaryIO) -> None:
        io.write(pack('>f', value))

    @classmethod
    def load(cls, io: BinaryIO) -> float:
        value, = unpack('>f', io.read(4))
        return value


class String(Serializer, hint=str):
    @classmethod
    def convert(cls, value: Any) -> str:
        assert isinstance(value, (str, bytes, bytearray))
        if isinstance(value, str):
            return value
        else:
            return value.decode()

    @classmethod
    def dump(cls, value: str, io: BinaryIO) -> None:
        data = value.encode()
        size = len(data)
        UnsignedInteger.dump(size, io)
        io.write(data)

    @classmethod
    def load(cls, io: BinaryIO) -> str:
        size = UnsignedInteger.load(io)
        value = io.read(size).decode()
        return value


#


class Field(object):
    def __init__(self, descriptor: Type[Serializer], explicit: bool = False):
        self.__descriptor: Type[Serializer] = descriptor
        self.__explicit = explicit
        self.__owner: Optional[type] = None
        self.__name: Optional[str] = None

    def __repr__(self):
        if not self.__owner or not self.__name:
            super().__repr__()
        return '<field %s.%s at 0x%x>' % (self.__owner.__name__, self.__name, id(self))

    def __set_name__(self, owner: type, name: str):
        self.__owner = owner
        self.__name = name

    def __get__(self, instance: Any, owner: type) -> Any:
        if instance is None:
            return self
        return instance.__dict__[self.__name]

    def __set__(self, instance: Any, value: Any) -> None:
        value = self.__descriptor.convert(value)
        instance.__dict__[self.__name] = value

    def dump(self, instance: Any, owner: type, io: BinaryIO) -> None:
        value = self.__get__(instance, owner)
        if self.__explicit:
            cls = SerializerMeta.resolve_type(value)
            uid = cls.uid
            io.write(pack('>I', uid))
        else:
            cls = self.__descriptor
        cls.dump(value, io)

    def load(self, instance, io: BinaryIO) -> None:
        if self.__explicit:
            uid, = unpack('>I', io.read(4))
            cls = SerializerMeta.resolve_uid(uid)
        else:
            cls = self.__descriptor
        value = cls.load(io)
        self.__set__(instance, value)

    @property
    def name(self):
        return self.__name

    @property
    def owner(self):
        return self.__owner


class AggregateMeta(SerializerMeta):
    @classmethod
    def __prepare__(mcs, name, bases):
        return OrderedDict()

    def __new__(mcs, name, bases, namespace, hint: Union[None, Type, Resolver] = None):
        if hint is None:
            hint = mcs._resolver
        return SerializerMeta.__new__(mcs, name, bases, namespace, hint)

    @classmethod
    def _resolver(mcs, value: Any) -> Optional[Type[Serializer]]:
        if isinstance(value, Aggregate):
            return type(value)
        return None


class Aggregate(Serializer, metaclass=AggregateMeta):
    @classmethod
    def convert(cls, value: Any) -> 'Aggregate':
        assert isinstance(value, cls)
        return value

    @classmethod
    def dump(cls, value: 'Aggregate', io: BinaryIO) -> None:
        assert isinstance(value, cls)
        fields = []

        for base in reversed(cls.__mro__):
            if not isinstance(base, AggregateMeta):
                continue
            attributes = base.__dict__.items()
            fields.extend(filter(lambda kv: isinstance(kv[1], Field), attributes))

        for name, field in fields:
            field.dump(value, cls, io)

    @classmethod
    def load(cls, io: BinaryIO) -> 'Aggregate':
        instance = cls.__new__(cls)
        for base in reversed(cls.__mro__):
            for name, field in base.__dict__.items():
                if not isinstance(field, Field):
                    continue
                field.load(instance, io)
        return instance


#


class A(Aggregate):
    x = Field(Integer)

    def __init__(self, x: int):
        self.x = x


class B(A):
    y = Field(Float)

    def __init__(self, x: int, y: float):
        super().__init__(x)
        self.y = y


class C(B):
    z = Field(String)

    def __init__(self, x: int, y: float, z: str):
        super().__init__(x, y)
        self.z = z


class D(Aggregate):
    x = Field(Integer)
    y = Field(A, True)

    def __init__(self, x: int, y: A):
        self.x = x
        self.y = y


#


def serialize(source):
    print('source = %r' % source)

    stream = BytesIO()
    Serializer.dump(source, stream)

    data = stream.getvalue()
    print(' '.join(map(lambda x: '%02x' % x, data)))

    stream = BytesIO(data)
    result = Serializer.load(stream)
    print('result = %r' % result)
    print()
    return result


#


x = 0
y = C(1, 2.0, '3')
source = D(x, y)
result = serialize(source)
