class Property(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func(instance)


class A(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @Property
    def z(self):
        return self.x + self.y


a = A(1, 2)
print(a.z)
