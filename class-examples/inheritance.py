class A(object):
    def foo(self):
        print('A.foo()')


class B(A):
    def __init__(self, x):
        self.x = x

    def bar(self):
        print('B.bar()')


class C(B):
    def __init__(self, x, y):
        B.__init__(self, x)
        self.y = y

    def foo(self):
        print('C.foo()')

    def baz(self):
        print('C.baz()')


a = A()
b = B(1)
c = C(2, 3)

a.foo()
b.foo()
c.foo()
input('Press Enter to continue...')

# a.bar()  # error!
b.bar()
c.bar()

input('Press Enter to continue...')

# a.baz()  # error!
# b.baz()  # error!
c.baz()
