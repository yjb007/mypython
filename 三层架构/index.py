#! /usr/bin/env python
#_*_ coding:utf-8 _*_

from module.userinfo import userinfo

def menu():
    user = raw_input('username:')
    pwd = raw_input('password:')
    
    UserInfo = userinfo()
    res = UserInfo.CheckUserInfo(user,pwd)
    print res
    



if __name__ == '__main__':
    menu()
    
#流程理解
'''
menu()输入，然后通过CheckUserInfo()检测输入正确与否

CheckUserInfo()查询表userinfo是否有相应的username和password

CheckUserInfo()定义了查询语句和传参了输入的用户名和密码

CheckUserInfo()连接数据库使用了哪些连接参数，调用的sql_helper SQL助手


'''

