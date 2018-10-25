from functools import reduce


goods = [
    {'name': 'apple', 'type': 'fruit', 'count': 1},
    {'name': 'orange', 'type': 'fruit', 'count': 2},
    {'name': 'banana', 'type': 'fruit', 'count': 3},
    {'name': 'tomato', 'type': 'vegetable', 'count': 4},
    {'name': 'carrot', 'type': 'vegetable', 'count': 5}
]

fruit_types = reduce(lambda x, y: 1 + x, filter(lambda x: x['type'] == 'fruit', goods), 0)
print('%d fruit types' % fruit_types)

veggi_types = reduce(lambda x, y: 1 + x, filter(lambda x: x['type'] == 'vegetable', goods), 0)
print('%d vegetable types' % veggi_types)

fruit_count = reduce(lambda x, y: x + y, map(lambda x: x['count'], filter(lambda x: x['type'] == 'fruit', goods)))
print('%d fruits in total' % fruit_count)

veggi_count = reduce(lambda x, y: x + y, map(lambda x: x['count'], filter(lambda x: x['type'] == 'vegetable', goods)))
print('%d vegetables in total' % veggi_count)
