from threading import *
from time import sleep


def print1():
    for i in range(50):
        print("thread #1: %d" % i)
        sleep(0.1)
    print("thread #1: exit")


def print2():
    for i in range(50):
        print("thread #2: %d" % i)
        sleep(0.1)
    print("thread #2: exit")


thread1 = Thread(target=print1)  # функция print1 будет вызвана в отдельном потоке
thread2 = Thread(target=print2)  # функция print2 будет вызвана в отдельном потоке
thread1.start()
thread2.start()


for i in range(50):
    print("main thread: %d" % i)
    sleep(0.1)
print("main thread: exit")
