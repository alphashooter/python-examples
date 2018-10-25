def generator(n):
    for i in range(1, n+1):
        yield i


iterator = generator(5)
while True:
    try:
        value = next(iterator)
    except StopIteration:
        break

    print(value)
