from random import randint
from itertools import count


target = randint(1, 10)
print('Отгадай число от 1 до 10')

for i in count(1):
    num = int(input(f'Попытка #{i}: '))
    if num == target:
        print('Угадал!')
        break
    else:
        print('Неугадал!')
