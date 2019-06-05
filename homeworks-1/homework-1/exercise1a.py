x = int(input('Введите число: '))

xmin = x % 10
xmax = x % 10
x //= 10

while x > 0:
    digit = x % 10
    if digit < xmin:
        xmin = digit
    if digit > xmax:
        xmax = digit
    x //= 10

print('Наименьшая цифра: %d' % xmin)
print('Наибольшая цифра: %d' % xmax)
