s = input('Введите число: ')

digits = map(lambda ch: int(ch), s)
digits = tuple(digits)

print(digits)
print('Наименьшая цифра: %s' % min(digits))
print('Наибольшая цифра: %s' % max(digits))
