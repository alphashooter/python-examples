from asyncio import *
import time


async def print1():
    for i in range(50):
        print("coroutine-1: %d" % i)
        await sleep(0.1)  # это sleep не из модуля time, а из модуля asyncio
    print("coroutine-1: exit")


async def print2():
    for i in range(50):
        print("coroutine-2: %d" % i)
        await sleep(0.1)
    print("coroutine-2: exit")


loop = get_event_loop()

print("calling print1...")
future1 = print1()  # без await вернется объект future, а не результат функции print1

print("calling print2...")
future2 = print2()  # без await вернется объект future, а не результат функции print2

# await print1()  # error: await можно использовать только внутри корутин
# await print2()  # error: await можно использовать только внутри корутин

# хотя print1 и print2 уже были вызваны,
# в консоли не будет ни одного сообщения:
# корутина не начинает работу, пока future не передан в loop,
# поэтому даже несмотря на time.sleep(1)
# после "calling print1..." и "calling print2..." будет сразу выведено "awake!"
time.sleep(1)
print("awake!")

task = gather(future1, future2)  # gather превращает несколько объектов future в один
loop.run_until_complete(task)  # print1 и print2 начнут работу только сейчас
print("done")  # loop.run_until_complete не вернет управление программе, пока task не будет выполнен
