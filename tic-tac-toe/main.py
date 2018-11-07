from tictactoe import *


def clear_screen():
    print('\n' * 20)


field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

markers = 'X', 'O'
player = 0

for i in range(9):
    player = (player + 1) % 2
    marker = markers[player]

    clear_screen()
    print_field(field)
    print('\nХодит %s.' % marker)

    while True:
        try:
            y = int(input('Введите строку: '))
            x = int(input('Введите стобец: '))
        except:
            print('Неверный ввод.')
            continue

        if not check_range(x, y):
            print('Координата (%d, %d) находится за пределами поля.' % (x, y))
            continue

        if not make_turn(field, marker, x, y):
            print('Клетка (%d, %d) занята.' % (x, y))
            continue

        break

    if check_field(field, marker):
        clear_screen()
        print_field(field)
        print('\nВыиграл %s.' % marker)
        break
else:
    clear_screen()
    print_field(field)
    print('\nНичья.')
