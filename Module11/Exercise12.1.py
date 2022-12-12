import socket

url = input("Enter a website URL: ")

try:
    parts = url.split('/')
    host = parts[2]
except:
    print("Invalid URL")
    exit()

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
except:
    print("Unable to connect to host")
    exit()

cmd = 'GET / HTTP/1.0\r\nHost: ' + host + '\r\n\r\n'
encoded = cmd.encode()
mysock.send(encoded)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

mysock.close()