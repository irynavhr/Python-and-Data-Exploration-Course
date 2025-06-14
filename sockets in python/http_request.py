import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect(("python.org", 80))

request = "GET / HTTP/1.1\r\nHost: python.org\r\n\r\n"
mysocket.send(request.encode())
response = mysocket.recv(1024)
print(response.decode())

mysocket.close()