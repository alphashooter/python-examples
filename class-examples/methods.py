class Foo(object):
    x = 1  # static property

    def __init__(self):
        self.y = 2  # instance property

    def instance_method(self):
        print('instance method:')
        print('x = %d, y = %d' % (self.x, self.y))  # instance method can use both static and instance properties
        print()

    @classmethod
    def class_method(cls):
        print('class method:')
        # y = cls.y  # fixme: class method cannot use instance properties
        x = cls.x  # but can use static through cls
        print('x = %d, y = ?' % x)
        print()

    @staticmethod
    def static_method():
        print('static method:')
        # y = Foo.y  # fixme: class method cannot use instance properties
        x = Foo.x  # but can use static through class Foo
        print('x = %d, y = ?' % x)
        print()


class Bar(Foo):
    x = 2  # todo: static property override


"""
Calling of instance/class/static methods:
"""
# both class and static methods can be used through any Foo instance
x = Foo()
x.instance_method()  # call instance method through a Foo instance
x.class_method()  # call class method through a Foo instance
x.static_method()  # call static method through a Foo instance

# both class and static methods can be called through Foo class
# Foo.instance_method()  # error
Foo.class_method()  # call class method through Foo class
Foo.static_method()  # call static method through Foo class


"""
Difference between instance/class/static methods:
"""
y = Bar()
y.instance_method()  # x = 2
y.class_method()  # x = 2
y.static_method()  # todo: x = 1, but Bar.x = 2...

Bar.class_method()  # x = 2
Bar.static_method()  # todo: x = 1, but Bar.x = 2...
