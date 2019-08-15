from socket import socket, AF_INET, SOCK_STREAM, IPPROTO_TCP, SHUT_WR

s = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP)
s.bind(('', 8080))
s.listen(5)

client, addr = s.accept()

req = client.recv(0x10000)
print(req.decode())
resp = (''
        'HTTP/1.0 200 OK\r\n'
        'Content-Type: image/jpeg\r\n'
        '\r\n')
client.send(resp.encode())
with open('image.jpg', 'rb') as file:
    client.send(file.read())
client.shutdown(SHUT_WR)
client.close()
