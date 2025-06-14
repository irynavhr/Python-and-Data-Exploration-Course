import socket

# Створити сокет (TCP, IPv4)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Вказати адресу й порт для прослуховування
server_socket.bind(('localhost', 5000))
server_socket.listen(1)  # До 1 клієнта одночасно

print("Сервер слухає порт 5000...")

conn, addr = server_socket.accept()  # Чекає на підключення
print(f"Підключився клієнт: {addr}")

# Отримати дані (1024 байти максимум)
data = conn.recv(1024)
print("Отримано:", data.decode())

# Відповісти клієнту
conn.sendall(b"hey from server!")

conn.close()
server_socket.close()
