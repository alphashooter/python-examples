from socket import getaddrinfo, socket, SHUT_WR, SOCK_STREAM, IPPROTO_TCP


def request(host: str) -> str:
    # resolve socket configuration
    infos = getaddrinfo(host, 80, 0, SOCK_STREAM, IPPROTO_TCP, 0)
    family, socktype, proto, canonname, addr = infos[0]

    # create socket
    connection = socket(family, socktype, proto)
    # connect to remote server
    connection.connect(addr)

    # write HTTP request into socket
    data = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    connection.sendall(data.encode())
    # flash all pending data and send EOF
    connection.shutdown(SHUT_WR)

    result = b''
    while True:
        data = connection.recv(4096)
        if not data:
            # received EOF
            break
        result += data

    connection.close()
    return result.decode()


print(request('google.com'), end='\n\n')
print(request('www.google.com'), end='\n\n')
print(request('wikipedia.org'), end='\n\n')
