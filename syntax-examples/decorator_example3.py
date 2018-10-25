from itertools import chain


def negate(fn):
    def wrapper(*args, **kwargs):
        return -fn(*args, **kwargs)
    wrapper.__name__ = 'negated_%s' % fn.__name__
    return wrapper


def print_call(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        fn_name = fn.__name__
        fn_args = chain(map(str, args), map(lambda key: '%s=%s' % (key, kwargs[key]), kwargs))
        fn_call = '%s(%s)' % (fn_name, ', '.join(fn_args))
        print('%s -> %s' % (fn_call, result))
        return result
    wrapper.__name__ = 'print_%s' % fn.__name__
    return wrapper


@print_call
def func1(x, y):
    return x + y


@print_call
@negate
def func2(x, y):
    return x + y


@negate
@print_call
def func3(x, y):
    return x + y


print('result = %d\n' % func1(1, 2))
print('result = %d\n' % func2(1, 2))
print('result = %d\n' % func3(1, 2))
