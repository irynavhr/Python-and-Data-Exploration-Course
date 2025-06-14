import socket
import ssl

host = 'example.com'
port = 443

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5)  # 5 секунд таймаут на підключення/очікування

context = ssl.create_default_context()
ssl_sock = context.wrap_socket(sock, server_hostname=host)

ssl_sock.connect((host, port))
request = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n"
ssl_sock.sendall(request.encode())

response = b''
try:
    while True:
        data = ssl_sock.recv(4096)
        if not data:
            break
        response += data
except socket.timeout:
    print('Таймаут: не отримано більше даних!')

print(response.decode(errors='replace'))
ssl_sock.close()
