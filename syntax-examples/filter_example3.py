def filter(pred, iterable):
    for x in iterable:
        print('filter x = %d' % x)
        if pred(x):
            print('yield %d!' % x)
            yield x
    print('filter end')


def predicate(x):
    return x > 0


seq = 1, 0, 2, 0, 3, 0, 4, 0, 5, 0
for value in filter(predicate, seq):
    print('for-in x = %d' % value)
print('for-in end')
