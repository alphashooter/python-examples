def min(arg, *args, value_to_key=None, **kwargs):
    if value_to_key is None:
        value_to_key = lambda x: x

    if len(args) > 0:
        values = args
        min_value, min_key = arg, value_to_key(arg)
        has_initial_value = True
    else:
        values = arg
        min_value, min_key = None, None
        has_initial_value = False

    value_key_pairs = tuple(map(lambda x: (x, value_to_key(x)), values))

    for value, key in value_key_pairs:
        if has_initial_value:
            if key < min_key:
                min_value, min_key = value, key
        else:
            min_value, min_key = value, key
            has_initial_value = True

    if not has_initial_value:
        if 'default' in kwargs:
            return kwargs['default']
        raise ValueError('arg is an empty sequence')

    return min_value


empty_sequence = tuple()
value_sequence = 3, 1, 2
x, y, z = value_sequence

print(min(x, y, z))  # result: 1
print(min(value_sequence))  # result: 1

print(min(x, y, z, value_to_key=lambda v: -v))  # result: 3
print(min(value_sequence, value_to_key=lambda v: -v))  # result: 3

print(min(x, y, z, default=0xE0F))  # result: 1
print(min(value_sequence, default=0xE0F))  # result: 1
print(min(empty_sequence, default=0xE0F))  # result: 3599

print(min(empty_sequence))  # error!
