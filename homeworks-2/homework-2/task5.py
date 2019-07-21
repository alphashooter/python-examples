def chain(iterable1, *args):
    for iterable in (iterable1, *args):
        for item in iterable:
            yield item


for x in chain(range(3), range(1, 4), range(2, 5)):
    print(x)
