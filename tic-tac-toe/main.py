import os
import sys
import pickle
from os.path import isfile
from tictactoe import *


def clear_screen():
    print('\n' * 20)


markers = 'X', 'O'

field = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
player = 0
turn = 0

if isfile('game.save'):
    # load field
    with open('game.save', 'rb') as file:
        field = pickle.load(file)
    os.remove('game.save')

    # calculate turn
    for row in field:
        for marker in row:
            if marker != ' ':
                turn += 1

    # calculate player
    player = turn % 2


for i in range(turn, 9):
    player = (player + 1) % 2
    marker = markers[player]

    clear_screen()
    print_field(field)
    print('\nХодит %s.' % marker)

    while True:
        try:
            y = int(input('Введите строку: '))
            x = int(input('Введите стобец: '))
        except (KeyboardInterrupt, EOFError):
            # save field
            with open('game.save', 'wb') as file:
                pickle.dump(field, file)
            sys.exit()
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
