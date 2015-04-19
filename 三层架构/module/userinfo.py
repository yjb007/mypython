#! /usr/bin/env python
#_*_ coding:utf-8 _*_

from utility.sql_helper import MysqlHelper


class userinfo(object):
    
    def __init__(self):
        self.__helper = MysqlHelper()
         
    def CheckUserInfo(self,username,password):
        sql = 'select * from userinfo where username = %s and password = %s'
        params = (username,password)
        return self.__helper.Get_One(sql,params)
    
        
        
        
        