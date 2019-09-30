from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, SHUT_WR
from select import select
from asyncio import get_event_loop, sleep


async def run_client(client: socket):
    client.setblocking(False)
    while True:
        r, w, x = select([client], [], [], 0.1)
        if client not in r:
            await sleep(0)
            continue
        print('received data')
        data = client.recv(0x1000)
        if not data:
            break
        client.send(data)
    client.shutdown(SHUT_WR)
    client.close()


async def run_server():
    server = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    server.bind(('', 10000))
    print('server started')
    server.listen(5)
    while True:
        r, w, x = select([server], [], [], 0.01)
        if server not in r:
            await sleep(0)
            continue
        client, addr = server.accept()
        print('accepted client')
        get_event_loop().create_task(run_client(client))


get_event_loop().run_until_complete(run_server())
