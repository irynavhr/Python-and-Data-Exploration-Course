import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('localhost', 5000))  # Підключення до сервера

client_socket.sendall(b"hey server!")
data = client_socket.recv(1024)
print("Відповідь сервера:", data.decode())

client_socket.close()
