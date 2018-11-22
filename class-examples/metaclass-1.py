class Foo(object):
    def __init__(self, x):
        self.x = x


class Bar(Foo):
    def f(self):
        print('Bar.f(): %d' % self.x)


#


instance = Bar(123)
print(type(instance))
print(Bar.f)
print(instance.f)
instance.f()
