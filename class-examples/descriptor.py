class RevealAccess(object):
    def __set_name__(self, owner, name):
        self.name = name
        self.owner = owner

    def __get__(self, instance, owner):
        if instance is None:
            return self
        value = instance.__dict__[self.name]
        print(
            'Read value %r from %s.%s through an instance of class %s' %
            (value, self.owner.__name__, self.name, owner.__name__)
        )
        return value

    def __set__(self, instance, value):
        print(
            'Write value %r into %s.%s through an instance of class %s' %
            (value, self.owner.__name__, self.name, instance.__class__.__name__)
        )
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        value = instance.__dict__[self.name]
        print(
            'Delete value %r from %s.%s through an instance of class %s' %
            (value, self.owner.__name__, self.name, instance.__class__.__name__)
        )
        del instance.__dict__[self.name]


class Foo(object):
    x = RevealAccess()


class Bar(Foo):
    pass


foo = Foo()
foo.x = 123  # RevealAccess.__set__
x = foo.x  # RevealAccess.__get__
del foo.x  # RevealAccess.__delete__


bar = Bar()
bar.x = x
x = bar.x
del bar.x
