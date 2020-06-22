def request(data: str, address: str, port: int = 80) -> str:
    from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, SHUT_WR
    with socket(AF_INET, SOCK_STREAM, IPPROTO_TCP) as s:
        s.connect((address, port))
        s.sendall(data.encode('utf-8'))
        s.shutdown(SHUT_WR)
        response = b''
        while True:
            packet = s.recv(4096)
            if not packet:
                break
            response += packet
        return response.decode('utf-8')
