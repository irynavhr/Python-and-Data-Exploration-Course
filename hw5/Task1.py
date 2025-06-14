# developed by Iryna Hrytsenko

import socket
import re
import ssl

url = input('Enter URL: ')

# check url
if not url.startswith('http://'):
    url = 'http://' + url

try:
    match = re.match(r'http://([^/]+)(/.*)?', url)
    if not match:
        raise ValueError("Invalid URL format")

    host = match.group(1)
    path = match.group(2) if match.group(2) else '/'
except Exception as e:
    print(f"Error parsing URL: {e}")

# socket
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))  
except Exception as e:
    print("Connection failed:", e)
    quit()

# request
cmd = f'GET {path} HTTP/1.0\r\nHost: {host}\r\n\r\n'
mysock.send(cmd.encode())

# count, read and save
count = 0
received  = b''
try:
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        count += len(data)
        received += data
except:
    print("Error reading from socket.")
    quit()
mysock.close()

# print
print(received[:1700].decode(errors='replace')) 
print(f"\nTotal characters received: {count}")
