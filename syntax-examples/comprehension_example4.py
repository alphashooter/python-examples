source = [
    [1, 2],
    [3, 4],
    [5, 6]
]
result = [value for row in source for value in row]
print(result)


for row in source:
    print(row)