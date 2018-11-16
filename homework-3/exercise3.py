import json
from os.path import isfile

# check if file exists
if isfile('persons.data'):
    # read persons from file
    with open('users', 'rb') as file:
        header = file.read(4)  # read 4-byte header
        data = file.read()  # read persons

    # check header
    if header == b'\xCA\xFE\xBA\xBE':
        # data is not encrypted
        persons = json.loads(data.decode())
    elif header == b'\x8B\xAD\xF0\x0D':
        # data is encrypted
        data = bytearray(map(lambda x: 255 - x, data))
        persons = json.loads(data.decode())
    else:
        # invalid header
        persons = {}
else:
    persons = {}


# print persons
print('Found %d records: ' % len(persons))
i = 1
for name in persons:
    print('{}. {}, {age}, {profession}'.format(i, name, **persons[name]))
print()


# add person
name = input('Enter name: ')
age = int(input('Enter age: '))
profession = input('Enter profession: ')
persons[name] = {'age': age, 'profession': profession}
# dump persons into json
data = json.dumps(persons).encode()


# write persons into file
encrypt = input('Do you want to encrypt data? (y/n)') == 'y'
with open('persons.data', 'wb') as file:
    if encrypt:
        header = b'\x8B\xAD\xF0\x0D'
        data = bytearray(map(lambda x: 255 - x, data))
    else:
        header = b'\xCA\xFE\xBA\xBE'
    file.write(header)
    file.write(data)
