from socket import socket, create_connection
from random import choice
from time import sleep


N = 10

clients = []
for i in range(N):
    clients.append(create_connection(('localhost', 10000)))

while True:
    client: socket = choice(clients)
    client.send(b'hello!')
    response = client.recv(6)
    print(response.decode())
    sleep(0.5)
