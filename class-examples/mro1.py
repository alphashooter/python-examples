def print_mro(obj):
    if isinstance(obj, type):
        obj_type = obj
    else:
        obj_type = type(obj)
    print(' -> '.join(map(lambda x: x.__name__, obj_type.__mro__)))


class A(object):
    pass


class B(A):
    pass


class C(B):
    pass


class D(C):
    pass


print_mro(D)
