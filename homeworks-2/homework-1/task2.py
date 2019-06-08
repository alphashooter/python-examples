n = int(input('n = '))

x1 = int(input('x1 = '))
x2 = int(input('x2 = '))
if x1 < x2:
    temp = x1
    x1 = x2
    x2 = temp

for i in range(2, n):
    x = int(input(f'x{i + 1} = '))
    if x > x1:
        x2 = x1
        x1 = x
    elif x > x2:
        x2 = x

print(x1, x2)
