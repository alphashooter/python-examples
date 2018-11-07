from random import randint


class A(object):
    def get_id(self):
        return 1


class B(A):
    def get_id(self):
        return 2


class C(A):
    def get_id(self):
        return 3


class D(B, C):
    def get_id(self):
        return 4


def create_instance() -> A:
    types = A, B, C, D
    factory = types[randint(0, 3)]
    return factory()


for i in range(10):
    instance = create_instance()
    value = instance.get_id()
    print(value, '(class %s)' % instance.__class__.__name__)
