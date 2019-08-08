import json


class SerializableMeta(type):
    def __new__(mcs, name, bases, namespace):
        excluded = set()
        for base in bases:
            if isinstance(base, SerializableMeta):
                excluded.update(base.__excluded__)
        if '__excluded__' in namespace:
            excluded.update(namespace['__excluded__'])
        namespace['__excluded__'] = tuple(excluded)
        return type.__new__(mcs, name, bases, namespace)


class Serializable(object, metaclass=SerializableMeta):
    def dump(self) -> bytes:
        fields = self.__dict__.copy()
        for field in self.__excluded__:
            if field in fields:
                del fields[field]
        s = json.dumps(fields)
        return s.encode()

    def load(self, data: bytes) -> None:
        s = data.decode()
        self.__dict__.update(json.loads(s))


class A(Serializable):
    def __init__(self, x):
        self.x = x


class B(Serializable):
    def __init__(self, y):
        self.y = y


class C(A, B):
    __excluded__ = '_C__z',

    def __init__(self, x, y):
        A.__init__(self, x)
        B.__init__(self, y)

    @property
    def z(self):
        if '_C__z' not in self.__dict__:
            self.__dict__['_C__z'] = self.x + self.y
        return self.__dict__['_C__z']


class D(C):
    pass


c = C(1, 2)
print(c.x, c.y, c.z)
print(c.dump())

d = D(1, 2)
print(d.x, d.y, d.z)
print(d.dump())

