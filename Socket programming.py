import socket

import addr as addr
import c

s = socket.socket()
print("socket created")
s.bind(('localhost', 9999))
s.listen(3)
print('waiting for the connection')
while True:
    c.addr = s.accept()
    print("connect with", addr)
    c.send(bytes('welcome to Naweed','utf-8'))
    c.close()

