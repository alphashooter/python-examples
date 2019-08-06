def f(self):
    print(self)


class Descriptor(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        def wrapper(*args):
            return self.func(instance, *args)

        return wrapper


class A(object):
    f = Descriptor(f)


a = A()
print(f"'f' in a.__dict__: {'f' in a.__dict__}")

value = None
for base in A.__mro__:
    print(f"'f' in {base.__name__}.__dict__: {'f' in base.__dict__}")
    if 'f' in base.__dict__:
        value = base.__dict__['f']
        break

getter = getattr(value, '__get__', None)
print(f"{base.__name__}.f.__get__: {getter}")

print(f"{base.__name__}.f.__get__(a, A): {getter(a, A)}")
print(f"a.f: {a.f}")
a.f()
