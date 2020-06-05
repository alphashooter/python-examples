from abc import abstractmethod


class Field(object):
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.convert(value)

    @abstractmethod
    def convert(self, value): ...

    @abstractmethod
    def dump(self, value): ...

    @abstractmethod
    def load(self, data: bytes): ...


class Integer(Field):
    def dump(self, value: int):
        return value.to_bytes(4, 'big')

    def load(self, data: bytes):
        return int.from_bytes(data[0:4], 'big')

    def convert(self, value):
        if isinstance(value, int):
            return value
        if isinstance(value, float):
            x = int(value)
            if x != value:
                raise ValueError()
            return x
        raise ValueError()


class Float(Field):
    def convert(self, value):
        if isinstance(value, float):
            return value
        if isinstance(value, int):
            return float(value)
        raise ValueError()

    def dump(self, value):
        from struct import pack
        return pack('>f', value)

    def load(self, data: bytes):
        from struct import unpack
        return unpack('>f', data[0:4])[0]


class Serializable(object):
    def dump(self) -> bytes:
        cls = self.__class__
        desc = {}
        for base in reversed(cls.__mro__):
            for key, value in base.__dict__.items():
                if isinstance(value, Field):
                    desc[key] = value
        result = b''
        for field in desc.values():
            result += field.dump(field.__get__(self, cls))
        return result

    @classmethod
    def load(cls, data: bytes) -> 'Test':
        ...
        obj = Test.__new__(Test)
        obj.__dict__.update(x)
        return obj


class Test(Serializable):
    x = Integer()
    _y = Float()

    def __init__(self, x: int, y: float):
        self.x: int = x
        self._y: float = y

    def __eq__(self, other):
        if not isinstance(other, Test):
            return False
        return self.x == other.x and self._y == other._y


x = 1
a = Test(1, 2)
data = a.dump()
print(data)
b = Test.load(data)
print(a == b)
