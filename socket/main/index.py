#! /usr/bin/env python
#_*_ coding:utf-8 _*_


import socket

def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello, World")
    #这个函数是发送给客户的数据
    
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
    #定义一个socket接口
    sock.bind(('localhost',8000))  
    #绑定的ip地址和端口
    sock.listen(5)
    #能接受的最大连接数

    while True:
        connection, address = sock.accept()
        #阻塞状态，直到有用户连接进来，用户请求，connection是客户端的socket对象，address是客户端的ip和端口,sock.accept()会返回两个变量赋值给connection, address
        #connection唯一标识一个客户端，这条命令就是一个变量赋值过程
        handle_request(connection)
        #服务器响应，调用handle_request函数
        connection.close()
        #断开连接，进行下一个链接

if __name__ == '__main__':
  main()

#http://localhost:8080/ 测试访问地址