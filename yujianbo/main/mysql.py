#! /usr/bin/env python
#_*_ coding:utf-8 _*_
import MySQLdb



########insert,update,delete########
conn = MySQLdb.connect(host = '10.0.18.1',user='root',passwd='123456',db='teacher');  
cur = conn.cursor();  

# param1 = raw_input('请输入你的名字：')
# param2 = input('请输入你的年龄：')
# sql = 'insert into teacher (name,age) values(%s,%s)'
# params = (param1,param2)
#使用变量插入数据

# sql = 'insert into teacher (name,age) values(%s,%s)'
# params = [('alex',24), ('sb',34),]
# reCount = cur.executemany(sql,params)
# conn.commit()
#插入多条数据，注意cur.executemany

sql = 'insert into teacher (name,age) values(%s,%s)'
params = ('user01','25')
#插入单条数据

# sql = 'update teacher set name=%s where teacher.age=%s;'
# params = ('user02',25)
#更新数据

# sql = 'delete from teacher where name=%s; '
# params = ('user02',)
#删除数据

reCount = cur.execute(sql,params)
conn.commit()
new_id =  cur.lastrowid
print new_id
#cur.lastrowid可以获取到insert数据的自增字段ID,可以把new_id作为变量导入带另外一个sql语句中，多表联合查询

cur.close()
conn.close()

# print reCount

#关于事物，同时提交多条语句后，再执行conn.commit()的，如果有一条语句执行失败，则conn.commit()会失败，默认启用事物

############select##############

conn = MySQLdb.connect(host = '10.0.18.1',user='root',passwd='123456',db='teacher');  
# cur = conn.cursor();  
cur = conn.cursor(cursorclass = MySQLdb.cursors.DictCursor)
#字典形式显示查找的内容

sql = 'select id,name,age from teacher where id = %s;'
params = (5,)
reCount = cur.execute(sql,params)
data = cur.fetchall()
print data

# sql = 'select * from teacher;'
# reCount = cur.execute(sql)

# data = cur.fetchone()
# print data
# #一次拿一条，下次运行则拿第二条，类似yield
# 
# cur.scroll(3,mode='absolute')
# #重新定位，3是返回第四条的意思，3,mode='absolute'，绝对位置，3指的是绝对位置是第四条，0，1，2，3，
# 
# data = cur.fetchone()
# print data
# cur.scroll(-1,mode='relative')
# #重新定位，3是返回相对本位置的下面3个位置，-1是返回相对本位置的上面1个位置，需要实际测试确定实际位置，相对位置
# 
# data = cur.fetchone()
# print data

cur.close()
conn.close()











