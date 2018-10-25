from functools import reduce


def min(arg, *args, key=None, **kwargs):
    if key is None:
        mapper = lambda x: (x, x)
    else:
        mapper = lambda x: (x, key(x))

    if args:
        vmin, kmin = reduce(lambda x, y: y if y[1] < x[1] else x, map(mapper, args), mapper(arg))
    else:
        try:
            vmin, kmin = reduce(lambda x, y: y if y[1] < x[1] else x, map(mapper, arg))
        except TypeError:
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
