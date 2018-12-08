from os.path import isfile
import sqlite3


if not isfile('test.db'):
    db = sqlite3.connect('test.db')
    db.execute('CREATE TABLE persons (name TEXT PRIMARY KEY, age INT, profession TEXT)')
    db.commit()
else:
    db = sqlite3.connect('test.db')


class Descriptor(object):
    def __set_name__(self, owner, name):
        self.column_name = name

    def __set__(self, instance, value):
        db.execute('UPDATE persons SET %s = ? where name = ?' % self.column_name, (value, instance.name))
        db.commit()
        instance.__dict__[self.column_name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self

        if self.column_name == 'name':
            return instance.__dict__[self.column_name]

        cursor = db.execute('SELECT ? FROM persons WHERE name = ?', (self.column_name, instance.name))
        return next(iter(next(cursor)))


class Person(object):
    name = Descriptor()
    age = Descriptor()
    profession = Descriptor()

    def __init__(self, name):
        self.__dict__['name'] = name
        cursor = db.execute('SELECT COUNT(*) FROM persons WHERE name = ?', (name,))
        count = next(iter(next(cursor)))
        if not count:
            db.execute('INSERT INTO persons(name) VALUES(?)', (name,))
            db.commit()


while True:
    try:
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        profession = input('Enter profession: ')
    except:
        print('Invalid input')
    else:
        break


person = Person(name)
person.age = age
person.profession = profession
