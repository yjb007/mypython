#! /usr/bin/env python
#_*_ coding:utf-8 _*_

import socket

sk = socket.socket()
ip_port = ('127.0.0.1',9999)
sk.bind(ip_port)
sk.listen(5)

while True:
    conn, addr = sk.accept()
    conn.send('hello')
    flag = True
    while flag:
        data = conn.recv(1024)
        if data == 'exit':
            flag = False
            conn.send('sexit')
        print data
        conn.send('sb')
    conn.close()


