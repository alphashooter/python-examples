from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, SHUT_WR
from select import select
from collections import deque


queue = deque()


def run_client(client: socket):
    client.setblocking(False)
    while True:
        r, w, x = select([client], [], [], 0.1)
        if client not in r:
            yield
            continue
        print('received data')
        data = client.recv(0x1000)
        if not data:
            break
        client.send(data)
    client.shutdown(SHUT_WR)
    client.close()


def run_server():
    server = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
    server.bind(('', 10000))
    print('server started')
    server.listen(5)
    while True:
        r, w, x = select([server], [], [], 0.01)
        if server not in r:
            yield
            continue
        client, addr = server.accept()
        print('accepted client')
        queue.append(run_client(client))


queue.append(run_server())
while queue:
    item = queue.popleft()
    try:
        next(item)
    except StopIteration:
        pass
    else:
        queue.append(item)
