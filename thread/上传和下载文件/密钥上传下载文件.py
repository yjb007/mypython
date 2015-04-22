#! /usr/bin/env python
#_*_ coding:utf-8 _*_

import paramiko

pravie_key_path = '/home/yjb007/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pravie_key_path)

t = paramiko.Transport(('10.0.18.2',22))
t.connect(username='root',pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.put('/tmp/test3.py','/tmp/test3.py') 

t.close()

import paramiko

pravie_key_path = '/home/yjb007/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(pravie_key_path)

t = paramiko.Transport(('10.0.18.2',22))
t.connect(username='root',pkey=key)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.get('/tmp/test3.py','/tmp/test4.py') 

t.close()