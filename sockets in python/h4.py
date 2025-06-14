import socket
import ssl

host = 'example.com'
port = 443

socket1 = socket.create_connection((host, port))
socket2 = ssl.create_default_context().wrap_socket(socket1, server_hostname=host)

request = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"
socket2.sendall(request.encode())

response = b''

while True:
    data = socket2.recv(4096)
    if not data:
        break
    response += data

print(response.decode(errors='replace'))
socket2.close()