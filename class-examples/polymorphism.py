class A(object):
    def __init__(self, value):
        self.value = value

    def foo(self):
        print('A.value = %s' % self.value)


x, y, z = A(1), A(2), A(3)

x.foo()
y.foo()
z.foo()
