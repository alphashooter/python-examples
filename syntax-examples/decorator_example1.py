def negate(fn):
    def wrapper(*args, **kwargs):
        return -fn(*args, **kwargs)
    return wrapper


@negate
def func(x, y):
    return x + y


result = func(1, 2)
print('result = %d' % result)
