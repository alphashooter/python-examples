# Пользователь вводит n
# Программа выводит список чисел от 1 до n

while True:
    try:
        n = int(input('n = '))
    except ValueError:
        print('Неверный ввод')
    else:
        break

print([*range(1, n + 1)])
