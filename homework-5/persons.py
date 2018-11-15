from os.path import isfile
import sqlite3


def load_persons(database):
    cursor = database.execute('SELECT name, age, profession FROM persons')
    return {name: {'age': age, 'profession': profession} for name, age, profession in cursor}


if not isfile('test.db'):
    db = sqlite3.connect('test.db')
    db.execute('CREATE TABLE persons (name TEXT PRIMARY KEY, age INT, profession TEXT)')
    db.commit()
else:
    db = sqlite3.connect('test.db')

persons = load_persons(db)
print(persons)

while True:
    try:
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        profession = input('Enter profession: ')
    except:
        print('Invalid input')
    else:
        break

if name in persons:
    pass  # do update
else:
    pass  # do insert
db.commit()

persons = load_persons(db)
print(persons)
