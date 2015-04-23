#! /usr/bin/env python
#_*_ coding:utf-8 _*_

import select
import socket
import sys
import Queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
#设置socket模式为非阻塞模式
#客户端可以连上，但不能交互数据
#不是完全非阻塞模式

server_address = ('localhost',10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
server.bind(server_address)

server.listen(5)
#socket队列最多是5个


