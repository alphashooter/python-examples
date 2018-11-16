from typing import Set, List
from random import randint
from functools import reduce


def unite(x: Set, y):
    x.add(y)
    return x


def reverse(x: List, y):
    x.insert(0, y)
    return x


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
predicates = {
    'evens': lambda x: x % 2 == 0,
    'odds': lambda x: x % 2 == 1,
    'simples': lambda x: x in {1, 2, 3, 5, 7}
}


n = int(input('Enter n: '))

# generate N random values
values = [randint(1, 9) for i in range(n)]
print(values)

# read actions
reducer_name, mapper_name, predicate_name = input('Enter action: ').split()

reducer, initializer = reducers[reducer_name]
mapper = mappers[mapper_name]
predicate = predicates[predicate_name]

result = reduce(reducer, map(mapper, filter(predicate, values)), initializer())
print(result)
