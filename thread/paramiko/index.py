#! /usr/bin/env python
#_*_ coding:utf-8 _*_
import paramiko

ssh = paramiko.SSHClient()
#实例化一个对象
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#让ssh远程登陆时的提问yes/no忽略掉
ssh.connect('10.0.18.1', 22, 'root', '123456')
#远程连接
stdin, stdout, stderr = ssh.exec_command('df')
#远程执行命令的返回内容，变量定义
print stdout.read()
#独处标准输出
ssh.close();
#关闭连接