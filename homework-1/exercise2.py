n = int(input('Введите n: '))

sum = 0

for i in range(n):
    x = int(input('Введите число #%d: ' % (i + 1)))
    if x % 3 == 0:
        sum += x

print('Сумма: %d' % sum)
