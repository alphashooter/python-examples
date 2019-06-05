from random import random, randint
from linked_list import LinkedList


seq1 = LinkedList()
seq2 = []
size1 = randint(50, 100)
size2 = randint(size1 // 3, size1 // 2)
size3 = randint(size2, size1)
size4 = randint(size2 // 3, size2 // 2)


def check(size):
    assert len(seq1) == len(seq2) == size
    for i in range(size):
        value1, value2 = seq1[i], seq2[i]
        assert value1 == value2
    print(seq2)


def insert(n):
    for i in range(n):
        value = randint(-100, 100)
        index = randint(0, i)

        r = random()
        if r < 0.5:
            seq1.append(value)
            seq2.append(value)
        else:
            seq1.insert(index, value)
            seq2.insert(index, value)


def erase(size, n):
    for i in range(n):
        r = random()
        if r < 0.33:
            index = 0
        elif r < 0.67:
            index = size - i - 1
        else:
            index = randint(0, size - i - 1)

        del seq1[index]
        del seq2[index]


# test 1
insert(size1)
check(size1)

# test 2
erase(size1, size1 - size2)
check(size2)

# test 3
insert(size3 - size2)
check(size3)

# test 4
erase(size3, size3)
check(0)

# test 5
insert(size4)
check(size4)
