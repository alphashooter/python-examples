def foo(x, y, z=2):
    return x + y + z


def bar(x, y):
    return x * y


print(foo(2, 3))  # 2 + 3 = 5
print(bar(2, 3))  # 2 * 3 = 6
print(foo(bar(2, 3), 4))  # (2 * 3) + 4 = 10
