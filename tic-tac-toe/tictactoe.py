def print_field(field):
    print('    1   2   3  ')
    print('  +---+---+---+')
    print('1 | %s |' % ' | '.join(field[0]))
    print('  +---+---+---+')
    print('2 | %s |' % ' | '.join(field[1]))
    print('  +---+---+---+')
    print('3 | %s |' % ' | '.join(field[2]))
    print('  +---+---+---+')


def check_range(x, y):
    return 1 <= x <= 3 and 1 <= y <= 3


def make_turn(field, value, x, y):
    if field[y - 1][x - 1] != ' ':
        return False
    field[y - 1][x - 1] = value
    return True


def check_rows(field, value):
    for i in range(3):
        if field[i][0] == field[i][1] == field[i][2] == value:
            return True
    return False


def check_cols(field, value):
    for i in range(3):
        if field[0][i] == field[1][i] == field[2][i] == value:
            return True
    return False


def check_diagonals(field, value):
    if field[0][0] == field[1][1] == field[2][2] == value:
        return True
    if field[0][2] == field[1][1] == field[2][0] == value:
        return True
    return False


def check_field(field, value):
    return check_rows(field, value) or check_cols(field, value) or check_diagonals(field, value)
