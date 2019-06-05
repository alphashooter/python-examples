from calendar import day_name, weekday


while True:
    try:
        date = input('Enter date (DD.MM.YYYY): ')
        day, month, year = map(int, date.split('.'))
    except:
        print('Invalid input')
    else:
        break

print(day_name[weekday(year, month, day)])
