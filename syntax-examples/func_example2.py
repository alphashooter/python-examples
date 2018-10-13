def foo(x, y=1):
    return x + y


print(foo(2, 3))  # 2 + 3 = 5
print(foo(2))  # foo(2) = foo(2, 1) = 2 + 1 = 3
