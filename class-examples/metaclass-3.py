class Method(object):
    def __init__(self, func, instance):
        self.func = func
        self.instance = instance

    def __call__(self, *args, **kwargs):
        self.func(self.instance, *args, **kwargs)


class Binding(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self.func
        return Method(self.func, instance)


#


class Foo(object):
    def __init__(self, x):
        self.x = x


def Bar_f(self):
    print('Bar.f(): %d' % self.x)


class BarMeta(type):
    def __new__(mcs, name, bases, namespace):
        result = type.__new__(mcs, name, bases, namespace)
        result.f = Binding(Bar_f)
        return result


class Bar(Foo, metaclass=BarMeta):
    pass


#


instance = Bar(123)
print(type(instance))
print(Bar.f)
print(instance.f)
instance.f()
