from typing import List
from socket import socket, create_connection
from time import sleep
from select import select

N = 10

sockets: List[socket] = []
for i in range(N):
    sockets.append(create_connection(('127.0.0.1', 5000)))


while True:
    for socket in sockets:
        r, w, x = select([socket], [], [], 0.05)
        if socket not in r:
            continue
        data = socket.recv(0x1000)
        sleep(1)
        socket.send(data)
