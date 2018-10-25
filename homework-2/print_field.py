data = [
    ['x', 'o', 'x'],
    ['o', ' ', 'x'],
    [' ', 'x', 'o']
]


def print_field(field):
    print('+---+---+---+')
    print('| %s |' % ' | '.join(field[0]))
    print('+---+---+---+')
    print('| %s |' % ' | '.join(field[1]))
    print('+---+---+---+')
    print('| %s |' % ' | '.join(field[2]))
    print('+---+---+---+')


print_field(data)
