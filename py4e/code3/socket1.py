import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# It is OK to use mysock = socket.socket() too.
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# encode(encoding='utf-8') or encode(encoding='ASCII') are both OK
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(), end='')

mysock.close()
