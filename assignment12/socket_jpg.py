# http://data.pr4e.org/cover3.jpg

import socket
import time

mysock = socket.socket()
mysock.connect(('data.pr4e.org', 80))
mysock.sendall('GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n'.encode())
picture = b''
count = 0

# Recive data
while True:
    data = mysock.recv(10240)
    if len(data) < 1:
        break
    picture = picture + data
    count = count + len(data)
    print(len(data), count)
    time.sleep(0.5)
mysock.close()

# cut head
head_end = picture.find(b'\r\n\r\n')
head = picture[:head_end]
print('Head lenth', head_end)
print(head.decode())

# paste image
picture = picture[head_end + 4:]
fhand = open('stuff_socket.jpeg', 'wb')
fhand.write(picture)
fhand.close()
