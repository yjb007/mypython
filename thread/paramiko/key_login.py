#! /usr/bin/env python
#_*_ coding:utf-8 _*_

import paramiko

private_key_path = '/home/yjb007/.ssh/id_rsa'
key = paramiko.RSAKey.from_private_key_file(private_key_path)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.0.18.2', 22,username=root, pkey=key)

stdin, stdout, stderr = ssh.exec_command('df -h')
print stdout.read()
ssh.close();
