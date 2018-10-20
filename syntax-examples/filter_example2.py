def filter(pred, iterable):
    for x in iterable:
        if pred(x):
            yield x


def predicate(x):
    return x > 0


seq = 1, 0, 2, 0, 3, 0, 4, 0, 5, 0
for value in filter(predicate, seq):
    print(value)
