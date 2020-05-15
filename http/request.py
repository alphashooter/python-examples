from socket import socket, create_connection, SHUT_WR

s = create_connection(('www.google.com', 80))
req = (''
       'GET / HTTP/1.0\r\n'
       'Host: www.google.com\r\n'
       '\r\n')
s.send(req.encode())
s.shutdown(SHUT_WR)
data = b''
while True:
    chunk = s.recv(0x20000)
    if not chunk:
        break
    data += chunk
s.close()
print(data.decode())
