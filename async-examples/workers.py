from threading import Thread, Lock, Condition
from collections import deque


class Promise(object):
    def __init__(self):
        self._lock = Lock()
        self._cv = Condition(self._lock)
        self._result = None
        self._error = None
        self._state = 0

    def get(self):
        with self._lock:
            self._cv.wait_for(lambda: self._state > 0)
            if self._state == 1:
                return self._result
            else:
                raise self._error

    def wait(self, timeout: float):
        with self._lock:
            return self._cv.wait_for(lambda: self._state > 0, timeout)

    def result(self, value):
        with self._lock:
            assert self._state == 0
            self._result = value
            self._state = 1
            self._cv.notify_all()

    def error(self, value):
        with self._lock:
            assert self._state == 0
            self._error = value
            self._state = 2
            self._cv.notify_all()


class Task(Promise):
    def __init__(self, target=None, args=None, kwargs=None):
        super().__init__()
        self._target = target
        self._args = args if args is not None else []
        self._kwargs = kwargs if kwargs is not None else {}

    def run(self):
        return self._target(*self._args, **self._kwargs)


class Manager(object):
    def __init__(self, n: int):
        self._queue = deque()
        self._lock = Lock()
        self._cv = Condition(self._lock)
        self._workers = []
        for i in range(n):
            worker = Worker(self)
            self._workers.append(worker)
            worker.start()

    def get_task(self) -> Task:
        with self._lock:
            self._cv.wait_for(lambda: len(self._queue) > 0)
            return self._queue.popleft()

    def add_task(self, task: Task):
        with self._lock:
            self._queue.append(task)
            self._cv.notify_all()


class Worker(Thread):
    def __init__(self, manager: Manager):
        super().__init__()
        self._manager = manager

    def run(self) -> None:
        while True:
            task = self._manager.get_task()
            try:
                result = task.run()
                task.result(result)
            except Exception as error:
                task.error(error)


def test(i):
    from random import random
    from time import sleep
    sleep(2 * random())
    return i


manager = Manager(2)
tasks = [Task(test, args=[i]) for i in range(10)]
for task in tasks:
    manager.add_task(task)
while tasks:
    for task in tasks:
        if task.wait(0.1):
            print(task.get())
            tasks.remove(task)
            break
