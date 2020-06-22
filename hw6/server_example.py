from hw6 import server


def handle_request(request: str) -> str:
    if request == 'GET / HTTP/1.0\r\n\r\n':
        return 'HTTP/1.0 200 OK\r\n\r\n'
    else:
        return 'HTTP/1.0 400 Bad Request\r\n\r\n'


server.serve(handle_request, '127.0.0.1', 8080)
