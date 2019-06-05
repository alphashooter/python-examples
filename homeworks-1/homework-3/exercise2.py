from typing import Set, List
from random import randint
from functools import reduce


def unite(x: Set, y):
    x.add(y)
    return x


def reverse(x: List, y):
    x.insert(0, y)
    return x


def evens(seq):
    for value in seq:
        if value % 2 == 0:
            yield value


def odds(seq):
    for value in seq:
        if value % 2 == 1:
            yield value


def simples(seq):
    for value in seq:
        if value in {1, 2, 3, 5, 7}:
            yield value


reducers = {
    'sum': (lambda x, y: x + y, lambda: 0),
    'multiply': (lambda x, y: x * y, lambda: 1),
    'join': (lambda x, y: 10 * x + y, lambda: 0),
    'unite': (unite, set),
    'reverse': (reverse, list)
}
mappers = {
    'negated': lambda x: -x,
    'inverted': lambda x: 1 / x,
    'squared': lambda x: x * x
}
generators = {
    'evens': evens,
    'odds': odds,
    'simples': simples
}


n = int(input('Enter n: '))

# generate N random values
values = [randint(1, 9) for i in range(n)]
print(values)

# read actions
reducer_name, mapper_name, generator_name = input('Enter action: ').split()

reducer, initializer = reducers[reducer_name]
mapper = mappers[mapper_name]
generator = generators[generator_name]

result = reduce(reducer, map(mapper, generator(values)), initializer())
print(result)
