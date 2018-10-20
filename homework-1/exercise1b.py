s = input('Введите число: ')

xmin = int(s[0])
xmax = int(s[0])

for ch in s:
    digit = int(ch)
    if digit < xmin:
        xmin = digit
    if digit > xmax:
        xmax = digit

print('Наименьшая цифра: %d' % xmin)
print('Наибольшая цифра: %d' % xmax)
