from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, SHUT_WR
from select import select
from asyncio import sleep, get_event_loop


async def communicate(client: socket, data):
    client.send(data)
    while True:
        r, w, x = select([client], [], [], 0.05)
        if client not in r:
            await sleep(0)
            continue
        return client.recv(0x1000)


async def echo(client: socket):
    client.setblocking(False)
    while True:
        await sleep(1)
        data = await communicate(client, b'hello!')
        print(data)


async def accept():
    server = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    server.bind(('', 5000))
    server.listen(5)
    server.setblocking(False)
    while True:
        r, w, x = select([server], [], [], 0.05)
        if server not in r:
            await sleep(0)
            continue
        client, addr = server.accept()
        get_event_loop().create_task(echo(client))


loop = get_event_loop()
loop.create_task(accept())
loop.run_forever()

