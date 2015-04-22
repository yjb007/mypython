#! /usr/bin/env python
#_*_ coding:utf-8 _*_

import os,sys
import paramiko

t = paramiko.Transport(('10.0.18.2',22))
t.connect(username='root',password='123456')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test.py','/tmp/test1.py')
#括号左边是代上传文件，右边是上传到服务器的哪个路径，名字是什么
t.close()


import os,sys
import paramiko

t = paramiko.Transport(('10.0.18.2',22))
t.connect(username='root',password='123456')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test1.py','/tmp/test2.py')
#括号左边是待下载的文件名称，右边是下载路径，名字是什么
t.close()



#对于python的伪多线程实际是单线程
#但在处理IO密集型时，因为硬盘速度慢，所以可以在处理磁盘IO时，可以先行处理别的线程
#多线程一定要加lock，因为数据出问题，event,处理好线程间的关系




