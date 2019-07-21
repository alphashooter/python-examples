import calendar
from datetime import datetime


target: int
while True:
    day_name = input(f'Enter day name ({calendar.day_name[0]}, etc.): ')
    for day, name in enumerate(calendar.day_name):
        if name == day_name:
            target = day
            break
    else:
        print('invalid input')
        continue
    break


now = datetime.now()
year, month = now.year, now.month

while True:
    if calendar.weekday(year, month, 1) == target:
        break
    month -= 1
    if month < 1:
        year -= 1
        month = 12


print(f'01.{month:02}.{year}')
