#! /usr/bin/env python
#_*_ coding:utf-8 _*_


import SocketServer
import os


class MyServer(SocketServer.BaseRequestHandler):
    def handle(self):
        base_path = 'D:/temp'
        conn = self.request
        print 'connected...'
        while True:
            pre_data = conn.recv(1024)
            
            cmd,file_name,file_size = pre_data.split('|')
            #获取请求方法、文件名、文件大小
            
            recv_size = 0
            #已经接收文件的大小
            
            file_dir = os.path.join(base_path,file_name)
            #上传文件路径拼接
            
            f = file(file_dir,'wb')
            Flag = True
            while Flag:
                
                if int(file_size)>recv_size:
                    #未上传完毕，
                    
                    data = conn.recv(1024) 
                    #最多接收1024，可能接收的小于1024
                    
                    recv_size+=len(data)
                
                else:
                    recv_size = 0
                    Flag = False
                    #上传完毕，则退出循环
                    
                f.write(data)
                #写入文件
            print 'upload successed.'
            f.close()
    
instance = SocketServer.ThreadingTCPServer(('127.0.0.1',9999),MyServer)
instance.serve_forever()








