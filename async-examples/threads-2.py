from threading import *
from time import sleep


lock = Lock()


def print1():
    for i in range(50):
        with lock:  # захват мьютекса перед вызовом print позволит избежать склеивания сообщений из разных потоков
            print("thread #1: %d" % i)
        # не вызывайте sleep и другие долгие операции с захваченным мьютексом,
        # поскольку все потоки, которые ждут его освобождения, остановятся
        sleep(0.1)
    with lock:
        print("thread #1: exit")


def print2():
    for i in range(50):
        with lock:
            print("thread #2: %d" % i)
        sleep(0.1)
    with lock:
        print("thread #2: exit")


thread1 = Thread(target=print1)
thread2 = Thread(target=print2)
thread1.start()
thread2.start()


for i in range(50):
    with lock:
        print("main thread: %d" % i)
    sleep(0.1)
with lock:
    print("main thread: exit")
