def min(arg, *args, key=None, **kwargs):
    if args:
        flag = False
        iterable = args
        if key is None:
            vmin, kmin = arg, arg
        else:
            vmin, kmin = arg, key(arg)
    else:
        flag = True
        iterable = arg
        vmin, kmin = None, None

    if key is None:
        iterable = map(lambda x: (x, x), iterable)
    else:
        iterable = map(lambda x: (x, key(x)), iterable)

    for v, k in iterable:
        if flag:
            vmin, kmin = v, k
            flag = False
        else:
            if k < kmin:
                vmin, kmin = v, k

    if flag:
        if 'default' in kwargs:
            return kwargs['default']
        raise ValueError('arg is an empty sequence')

    return vmin


empty_sequence = tuple()
value_sequence = 3, 1, 2
x, y, z = value_sequence

print(min(x, y, z))  # result: 1
print(min(value_sequence))  # result: 1

print(min(x, y, z, key=lambda v: -v))  # result: 3
print(min(value_sequence, key=lambda v: -v))  # result: 3

print(min(x, y, z, default=0xE0F))  # result: 1
print(min(value_sequence, default=0xE0F))  # result: 1
print(min(empty_sequence, default=0xE0F))  # result: 3599

print(min(empty_sequence))  # error!
