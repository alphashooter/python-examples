def negate(fn):
    def wrapper(*args, **kwargs):
        return -fn(*args, **kwargs)
    return wrapper


func = lambda x, y: x + y
func = negate(func)


result = func(1, 2)
print('result = %d' % result)
