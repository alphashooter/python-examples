from typing import Optional
from orm import Model
from sqlalchemy import Column, String, Integer


class Person(Model):
    __tablename__ = 'persons'

    name = Column(String, primary_key=True)
    age = Column(Integer)
    profession = Column(String)

    def __init__(self, name: str, age: Optional[int] = None, profession: Optional[str] = None):
        super().__init__()
        self.name = name
        self.age = age
        self.profession = profession

    def __repr__(self):
        return repr({'age': self.age, 'profession': self.profession})


#

def load_persons():
    return {person.name: person for person in Person.enumerate()}


persons = load_persons()
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
    person = persons[name]
    person.age = age
    person.profession = profession
else:
    person = Person(name, age, profession)
person.delete()

persons = load_persons()
print(persons)
