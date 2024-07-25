import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

response = b""
while True:
    data = mysock.recv(512)

    if len(data) < 1:
        break
    response += data

mysock.close()

response = response.decode()  

headers, body = response.split('\r\n\r\n',1)

print("Headers : \n", headers)
print("\nBody : \n",body)