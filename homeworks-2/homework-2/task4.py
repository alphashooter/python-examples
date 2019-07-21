def count(start, step=1):
    i = start
    while True:
        yield i
        i += step


for x in count(1, 2):
    print(x)
