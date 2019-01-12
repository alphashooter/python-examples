from threading import *
from time import sleep


print_lock = Lock()


def sync_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)


#


lock1 = Lock()
lock2 = Lock()


def deadlock1():
    sync_print("thread-1: trying to acquire lock1")
    with lock1:
        sync_print("thread-1: acquired lock1")

        sleep(1)  # в это время второй поток вызывает lock2.acquire()

        sync_print("thread-1: trying to acquire lock2")
        with lock2:  # поток не сможет захватить мьютекс lock2, потому что он захвачен вторым потоком
            sync_print("thread-1: acquired lock2")  # сообщение никогда не отобразится


def deadlock2():
    sync_print("thread-2: trying to acquire lock2")
    with lock2:
        sync_print("thread-2: acquired lock2")

        sleep(1)  # в это время первый поток вызывает lock1.acquire()

        sync_print("thread-2: trying to acquire lock1")
        with lock1:  # поток не сможет захватить мьютекс lock1, потому что он захвачен первым потоком
            sync_print("thread-2: acquired lock1")  # сообщение никогда не отобразится


thread1 = Thread(target=deadlock1)
thread2 = Thread(target=deadlock2)
thread1.start()
thread2.start()


# thread1 -> lock1.acquire() -> lock2.acquire()
# thread2 -> lock2.acquire() -> lock1.acquire()
# потоки заблокировали друг друга и никогда не смогут продолжить выполнение, а программа никогда не завершится
