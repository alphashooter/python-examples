from hw7 import client

data = 'GET / HTTP/1.0\r\n\r\n'
print(client.request(data, '127.0.0.1', 8080))
