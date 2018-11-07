from datetime import datetime
from calendar import weekday, day_name, month_name


def input_day() -> int:
    attempt = 0
    days = list(map(lambda x: x.lower(), day_name))
    while True:
        s = input('Enter day name (e.g. %s): ' % day_name[attempt])
        attempt = (attempt + 1) % 7
        try:
            return days.index(s.lower())
        except ValueError:
            print('"%s" is not a valid day name' % s)


def find_month_year(day):
    now = datetime.now()
    year = now.year
    month = now.month

    while True:
        if weekday(year, month, 1) == day:
            return month, year

        month -= 1
        if not month:
            month = 12
            year -= 1


day = input_day()
month, year = find_month_year(day)
print('%s, %d' % (month_name[month], year))
