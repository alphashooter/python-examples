from functools import reduce


goods = [
    {'name': 'apple', 'type': 'fruit', 'count': 1},
    {'name': 'orange', 'type': 'fruit', 'count': 2},
    {'name': 'banana', 'type': 'fruit', 'count': 3},
    {'name': 'tomato', 'type': 'vegetable', 'count': 4},
    {'name': 'carrot', 'type': 'vegetable', 'count': 5}
]

counts = list(map(lambda x: x['count'], goods))
print(counts)

total = reduce(lambda x, y: x + y, counts)
print(total)
