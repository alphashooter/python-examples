def print_seq(seq, highlight=-1):
    element = str(seq[0])
    if highlight == 0:
        line2 = '^' * len(element)
    else:
        line2 = ''
    line1 = element

    for i in range(1, len(seq)):
        element = str(seq[i])
        line1 += ', '
        if highlight == i:
            line2 = ' ' * len(line1) + '^' * len(element)
        line1 += element

    print('')
    print(line1)
    print(line2)


def print_del(count):
    tmp = count % 100
    if tmp > 20:
        tmp %= 10
    if tmp == 1:
        print('Удалено %d число' % count)
    elif 2 <= tmp <= 4:
        print('Удалено %d числа' % count)
    else:
        print('Удалено %d чисел' % count)


n = int(input('Введите n: '))
numbers = [i for i in range(1, n)]

i = 1
while numbers[i] < n / 2:
    counter = 0
    print_seq(numbers, i)

    for j in range(len(numbers) - 1, i, -1):
        if numbers[j] % numbers[i] == 0:
            print('%d делится на %d, удаление' % (numbers[j], numbers[i]))
            counter += 1
            del numbers[j]
        else:
            print('%d не делится на %d' % (numbers[j], numbers[i]))

    print_del(counter)
    i += 1

print_seq(numbers)
