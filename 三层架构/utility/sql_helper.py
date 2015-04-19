#! /usr/bin/env python
#_*_ coding:utf-8 _*_

import MySQLdb
import conf

class MysqlHelper(object):
    
    def __init__(self):
        self.__conn_dict = conf.conn_dict
    
    def Get_Dict(self,sql,params):
        
        conn = MySQLdb.connect(**self.__conn_dict);  
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

        reCount = cur.execute(sql,params)
        data = cur.fetchall()
        
        cur.close()
        conn.close()
        return data
        
    def Get_One(self,sql,params):
        
        conn = MySQLdb.connect(**self.__conn_dict);  #把字典当参数必须前面加**
        cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)

        reCount = cur.execute(sql,params)
        data = cur.fetchone()
        if data:
            return '登录OK'
        else:
            return '登录False'
        cur.close()
        conn.close()
#         return data
    
# helper = MysqlHelper()
# sql = 'select * from userinfo where username = %s and password = %s;'
# params = ('yjb007','123456')
# print helper.Get_Dict(sql, params)
# print helper.Get_One(sql, params)


        
        
        
        
        
        
        
        
        