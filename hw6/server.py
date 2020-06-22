from typing import Callable


def serve(handler: Callable[[str], str], address: str, port: int = 80) -> None:
    from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, SHUT_WR
    with socket(AF_INET, SOCK_STREAM, IPPROTO_TCP) as server:
        server.bind((address, port))
        server.listen()
        while True:
            client, addr = server.accept()
            with client:
                request = b''
                while True:
                    packet = client.recv(4096)
                    if not packet:
                        break
                    request += packet
                response = handler(request.decode('utf-8'))
                client.sendall(response.encode('utf-8'))
                client.shutdown(SHUT_WR)
