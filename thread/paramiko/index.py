#! /usr/bin/env python
#_*_ coding:utf-8 _*_
import paramiko

ssh = paramiko.SSHClient()
#ʵ����һ������
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#��sshԶ�̵�½ʱ������yes/no���Ե�
ssh.connect('10.0.18.1', 22, 'root', '123456')
#Զ������
stdin, stdout, stderr = ssh.exec_command('df')
#Զ��ִ������ķ������ݣ���������
print stdout.read()
#������׼���
ssh.close();
#�ر�����