class A(object):
    def foo(self):
        print('A.foo()')


class B(A):
    def bar(self):
        print('B.bar()')


class C(B):
    def foo(self):
        print('C.foo()')

    def baz(self):
        print('C.baz()')


a = A()
b = B()
c = C()

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
