import socket

host = 'python.org'
port = 80
page = '/'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

request = f"GET {page} HTTP/1.1\r\nHost: {host}\r\n\r\n"
client_socket.send(request.encode())

response = b''
while True:
    chunk = client_socket.recv(4096)
    if not chunk:
        break
    response += chunk

print(response.decode(errors='replace'))  # errors='replace' на випадок "недокодованих" символів
client_socket.close()
