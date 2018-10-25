seq = [1, 2, 3, 4, 5]


for value in seq:
    print(value)

print()  # just a newline

iterator = iter(seq)
while True:
    try:
        value = next(iterator)
    except StopIteration:
        break

    print(value)
