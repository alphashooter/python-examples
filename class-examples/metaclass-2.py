class Foo(object):
    def __init__(self, x):
        self.x = x


def Bar_f(self):
    print('Bar.f(): %d' % self.x)


name = 'Bar'
bases = Foo,
namespace = {'f': Bar_f}
Bar = type(name, bases, namespace)


#


instance = Bar(123)
print(type(instance))
print(Bar.f)
print(instance.f)
instance.f()
