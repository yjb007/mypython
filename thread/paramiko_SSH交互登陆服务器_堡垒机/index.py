#! /usr/bin/env python
#_*_ coding:utf-8 _*_

import paramiko

scp = paramiko.Transport(('182.92.219.86',22));
scp.connect(username='wupeiqi',password='xxx');
channel = scp.open_session();
print channel.exec_command('mkdir hello')
channel.close();
scp.close();

import paramiko
import interactive

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.1.108', 22, 'alex', '123')

channel = ssh.invoke_shell()
interactive.interactive_shell(channel)
channel.close()
ssh.close();






#开源软件，shellinabox,可以web方式进入shell