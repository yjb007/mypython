#! /usr/bin/env python
#_*_ coding:utf-8 _*_

from file import demo
from __builtin__ import dict
from random import random
import code
from test.test_hashlib import HashLibTestCase
import hashlib
from email.utils import getaddresses
from _pyio import __metaclass__
from ctypes.wintypes import MSG


reload(demo)

if __name__ == '__main__':
    demo.Foo()
else:
    print 'no'


print __file__
print __doc__
print __name__

def foo(name, action = '砍柴', where = '北京'):
    print name, '去', where, action
    
foo('张三', '吃饭', '上海')
foo('李四')
foo('王五', action = '上网')
foo('六六', action = '上网' , where='广州')

def show(*agrv):
    for i in agrv:
        print i
show(1,2,3,4,5)
#传参是不确定的多个参数

def show1(agrv):
    for item in agrv:
        print item
show1([1,2,3,4,5])
#传参是列表 

def show2(**agrv):
    for item in agrv.items():
        print item
        
dict={'k1':123, 'k2':'yjb','k3':'张三'}
print dict
show2(**dict)
show2(name='zhangsan', age=24)
#传参是字典



def login(username):
    if username == 'alex':
        return 'OK'
    else:
        return 'NO'
#return返回值
       
def detail(username): 
    print username, 'your money is 5555'
        
# if __name__ =='__main__':
#     user = raw_input('please input your name:')
#     res = login(user)
#     if res == 'OK':
#         detail(user)
#     else:
#         print 'NO MONEY'
    
    
def xxx():
    yield 1
    yield 2
    yield 3     
    yield 4   
    yield 5   

re = xxx()         
print re
#yield是生成器，可以不占用内存
for item in re:
    print item
    
    
def AlexReadlines():
    seek = 0 #变量seek
    while True:
        with open('E:/tmp.txt','rb') as f: #这样定义就不用f.close()了
            f.seek(seek)  #定位到位置0
            data = f.readline() #读取文件
            if data: #判断data是否存在
                seek = f.tell() #重新定义seek的位置，f.tell()定位出现在的文件的位置，为下次读取做准备
                yield data #将data保存到yield中,逐行读取并保存到data
            else:
                return  #return会退出整个脚本
  
print AlexReadlines() #打印出的是生成器
  
for item in AlexReadlines():
    print item,

#可用作线程池，迭代效果比较好
#一般函数只有函数执行完毕后才能返回，中间状态外界不知道
#yield可以让函数执行的中间过程的状态被外界所知         
    

    
result = 'false' if 1>3 else 'true'
print result
#三元运算符

def plus(x,y):
    return x+y
print plus(13, 34)

tmp = lambda x,y,z:x+y*z-x
print tmp(1,2,3)
#lambda运算符，匿名函数

print map(lambda x:x**2, range(10))

a = []
# help(a)
# help(dir())
print dir(a)
print type(a)
print vars() 

print abs(-9)     
#求绝对值

print cmp(3,3)
#比较大小

print bool(-1)
#只有0是假，其余都是真


print divmod(5, 2)
#求余数和商

print max(8,6,10)
print max([1,2,3,4,5,6,7])
print min(1,2,3,4,5,6)
print min([1,4,5,7,8,0,-4])
#取最大值,和最小值

print sum([1,2,3,4,5,6])
#求和

print pow(3, 4)
#3**4指数

print len('dsfsdf')
#字符的长度

print all([1,2,3,4,5,6])
#遍历所有元素，如果有0则为假，其余都是真

print any([1,2,3,4,5,6,0])
#遍历所有元素，如果有一个是真，则是真

print chr(66)
#根据asicc码查看字符

print ord('a')
print ord('G')
#查看字符的asicc码

print hex(2)
print bin(2)
print oct(2)
#转换成16进制，2进制，8进制

print range(5)
print xrange(5)
#打印一个数字列表
#xrange是一个生成器，减少内存占用

li = ['手表','汽车','房子']
for i in li:
    print i
    
for item in enumerate(li,1):
    print item[0],item[1]
#打印列表，并表示出序列号，1是起始序列值
#item[0],item[1]表示打印出第一列和第二列

for k,v in enumerate([1,2,3,4]):
    print k,v
#给列表排序加上序列号

s = 'i am {0} {1}'
print s.format('alex', 'xxx')
#占位符用法


alex = 'xx'
xxx = 'XXXX'
print  'i am %s %s'  %(alex, xxx)

def Function(arg):
    print arg
    
Function('yujianbo')




li = [11,22,33,44]
tmp = []
for item in li:
    tmp.append(item + 100)  
print tmp

###############################################
def yyy(arg):
    return arg + 100

li = [11,22,33,44]
tmp = []
for item in li:
    tmp.append(yyy(item))
  
print tmp
##########################

def yyy(arg):
    return arg + 100
tmp = map(yyy, li)
print tmp
#map函数，参数第一个跟函数名，后面跟需要遍历列表等，map将执行结果追加到一个列表里面

li = [11,22,33,44]
tmp = map(lambda arg:arg+100,li)
print tmp

#map对一个列表进行遍历，然后交给前面的函数进行处理，结果保存到一个列表里面

li = [11,22,33,44]
def fil(arg):
    if arg >= 22:
        return True
    else:
        return False

tmp = filter(fil, li)
print tmp
#filter过滤参数，只将过滤结果为true的函数处理结果放到新的列表中

li = [11,22,33,44]
tmp = reduce(lambda x,y:x+y, li)
print tmp
#x+y累加，x*y累乘，必须要接受两个参数下x，y

x = [1,2,3,4,5]
y = [5,6,7,8,9]
z = [3,5,7,9,0]
print zip(x,y,z)
#竖向成新列表

a = '8*8'
print eval(a)
#直接运算字符串运行，shell中也有类似的



tmp = 'mysqlhelper'
model = __import__(tmp)
model.count()
#反射，通过字符串模式导入模块，可以方便切换



tmp = 'mysqlhelper'
func = 'count'
model = __import__(tmp)
ggg = getattr(model, func)
print ggg()
#通过字符串模式导入函数，需要先找到函数getattr

import random
print random.random()
print random.random()*10
#生成0-1之间的随机数
print random.randint(1,5)
#生成1-5间的整形随机数

print random.randrange(1,3)
#生成1和2，不会生成3，整形

print random.randint(100000,999999)
#生成6位随机数

code = []
for i in range(6):
    if i == random.randint(1,5):
        code.append(str(random.randint(1,5))) 
    else:
        tmp = random.randint(65,90)
        code.append(chr(tmp))
print code
print ''.join(code)

#生成六位随机数，数字字符混合
#列表转字符串，非常有用，''.join(code)

import hashlib

hash = hashlib.md5()
hash.update('admin')
print hash.hexdigest()
print hash.digest()

#md5加密


import pickle

li = ['111','222','333','444']

dumped = pickle.dumps(li)
print dumped
print type(dumped)
#序列化一个列表,也可以序列化字典，类等，变成字符串，才能存到硬盘，

loaded = pickle.loads(dumped)
print loaded
print type(loaded)

#反序列化一个字符串，读到内存中

pickle.dump(li, open('D:/tmp.pk', 'wb'))
#将序列化结果保存到硬盘中

result = pickle.load(open('D:/tmp.pk','rb'))
print result
#将硬盘中的序列化文件进行反序列化

###################################################################

import json
name_dict = {'name':'yujianbo','age':24}
dumped = json.dumps(name_dict)
print dumped
#json的序列化

loaded = json.loads(dumped)
print loaded
print type(loaded)



with open('D:/tmp1.pk','wb') as f1:
    json.dump(name_dict,f1)

with open('D:/tmp1.pk','rb') as f2:
    result = json.load(f2)
print result

#json的序列化和反序列化

#pickle只是python用的格式，json所有程序都支持
#列表的序列化和反序列化，一般用在两个python程序之间进行数据交换










import re

res1 = re.match('\d+', 'adasdfd123asd231asdc12eadqwd')
res2 = re.search('\d+', 'sdfsdf123asd231asdc12eadqwd')
if res1:
    print res1.group()
else:
    print 'nothing'
    
if res2:
    print res2.group()

#match是从头匹配，search是全文查找


res3 = re.findall('\d+', 'asdfads1111dfsd2222sdfsd3444')
if res3:
    print res3

com = re.compile('\d+')
#生成一个对象,效率高
# print com.findall('asdfads1111dfsd2222sdfsd3444') 
# print com.search('asdfads1111dfsd2222sdfsd3444') 
# print com.match('3455asdfads1111dfsd2222sdfsd3444') 
#正则表达式

#\d代表数字，\w代表下划线，字母，横杠，\t除回车外所有字符，\是转义的意思


ip = '12.34.56.fsdfds.wefwef-1rdf-2ref2f2f_192.168.1.15sfsdfwef.ergergeg'
print ip

print re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',ip)
#[0-9]{1,3}\.  0-9出现1到3次，转义.


import time
print time.time()
#计算1970年之后的秒数

print time.gmtime()
#结构化格式化字符串，time.struct_time(tm_year=2015, tm_mon=4, tm_mday=17, tm_hour=11, tm_min=52, tm_sec=48, tm_wday=4, tm_yday=107, tm_isdst=0)

print time.strftime('%Y%m%d %H%M%S')
#20150417 195358时间格式

print time.strftime('%Y-%m-%d %H:%M:%S')
#2015-04-17 19:54:48

print time.strptime('2015-04-17', '%Y-%m-%d')
#格式转换，两个参数的格式要一致，会转换成结构化格式

print time.localtime()
#结构化格式

print time.mktime(time.localtime())
#结构化格式转秒数

print time.asctime(time.localtime())
print time.ctime(time.time())


# data = raw_input('请输入URL:')
data = 'test1/login'
#输入格式 xxx/xxx
array = data.split('/')
#分割字段成列表
userspance = __import__('main.'+array[0] )
#反射，导入其他模块，array可以是login，logout等模块
model1 = getattr(userspance, array[0])
#反射，导入其它模块
func = getattr(model1, array[1])
#导入其它模块的函数
func()

##例如输入test1/login
#生产环境可以将登陆，查询等设置成各自的模块函数，统一调用




###############装饰器################
def outer(fun):
    def wrapper(arg):
        print 'True'
        fun(arg)
        result = fun(arg)
        return result
        print 'False'
    return wrapper

@outer
def func1(arg):
    print 'func1',arg
    return 11111
#return返回值默认是不在控制台显示的，需要接受结果才能打印出来

# @outer
# def func2():
#     print 'func2'
#     
# @outer
# def func3():
#     print 'func3'

func1('ttt')
respones = func1('ttt')
print respones
# func2()
# func3()
'''
运行流程是将outer函数加载到内存中
然后遇到@outer，@outer = outer(func1)把func1当作outer的参数
则执行outer函数，将func1传参，将函数wrapper加载到内存中
执行outer函数的结果，返回值是wrapper整个函数
此时结果是func1函数被重新赋值成整个wrapper函数
然后执行函数wrapper
执行到fun()时，则去调用func1()函数

装饰器会一次将所有的@outer全部调用
'''

###############类############
class Province(object):
    #继承和不继承object
    mem = '是23个省之一'
    #静态字段
    
    def __init__(self,name,capital,leader,pri):  #构造函数。
        self.Name = name
        self.Capital = capital
        self.Leader = leader
        self.test = 'ggggggggggg'  #可以自定义，不用传参
        self.__PriName = pri   #私有字段，可以被动态方法调用，也可以被特性调用，数据库字符串
    #动态字段
    
    def sport_meet(self):
        print self.Name+'正在开运动会'

    def pri_method(self):
        print self.__PriName
        self.__sha()
        
    def Pri(self):
        print self.__PriName

     #动态方法
     
    def __sha(self):
        print 'i am pri method'
     #私有方法，只能被类中的其它方法调用，一般不能被外部调用
     
    @staticmethod
    def Fanfu():
        print '每个省都要带头反复'
    #静态方法
    
    @property
    def Bar(self):
        print self.Name
        print self.__PriName
        return 'hahaha'   #return放在最后，不然其它命令执行不了

        
    @Bar.setter   #这个装饰器可以将Bar函数里面的私有字段变成可写,修改某个字段的名称,私有字段或普通字段都可修改
    def Bar(self,value1):
        self.__PriName = value1
#         self.Name = value2

     #特性，默认值可读,一般只有在有私有字段时才使用特性
    
    
    

sd = Province('山东','济南','张三','鲁')
hb = Province('河北','石家庄','李四','冀')      

Province.Fanfu()
sd.sport_meet()
sd.pri_method()
hb.pri_method()
hb._Province__sha()   #强制调用私有方法
#方法调用

print sd.Name
print hb.Leader
print Province.mem
#字段调用
  
hb.Bar

# time.sleep(5)
#暂停5s

print sd.Pri  #可以在特性中调用私有字段
#调用特性方法
#通过print可以打印出返回值

print hb.Bar
hb.Bar = 'jiji'
print hb.Bar



###############抽象类###############

from abc import ABCMeta,abstractmethod
 
class Alter:
    __metaclass__ = ABCMeta
     
    @abstractmethod
    def sendmail(self):
        pass
     
class weinxin(Alter):
    def __init__ (self):
        print '__init__'
    
    def sendmail(self):
        print 'send.weixin'
    #子类必须有sendmail方法     
f = weinxin()
f.sendmail()




##########异常处理################

#data = raw_input('请输入URL:')
data = 'test1/login'
array = data.split('/')

try:
    userspance = __import__('main.'+array[0] )
    func = getattr(model1, array[1])
    func()

# except AttributeError,e:
#     print 1, e
#     print '这里有一个错误'
# 
# except ImportError,e:
#     print '2:', e
#     print '这里又有一个错误'

except Exception,e:
    print 3, e
    print '所有错误都在这'
#Exception所有错误都在这里

else:
    print '什么错误都没有'
    
finally:
    print '无论错误与否都继续执行'
    print time.strftime('%Y-%m-%d')
    

class MyException(Exception):
    def __init__(self,msg):
        self.error = msg
    
    def __str__(self, *args, **kwargs):
#         return Exception.__str__(self, *args, **kwargs)
        return self.error  #也可以自定义内容

#__str__函数，会有返回结果，直接丢给print obj显示，是obj实例化的一个介绍
    
obj = MyException('发生了一个错误')
print obj   #没有__str__函数则不会有任何显示

# raise MyException('自定义触发错误')




def login11(name,pwd):
    if name == 'yujianbo' and pwd == '123456':
        return True
    else:
        return False

try:
    res = login11('yujianbo', '1234567')
    if res:
        print 'login sucessful'
    else:
        print 'login failed'
        raise Exception('login failed in log')  #主动触发错误，则此自定义错误'login failed in log'会记录到Exception，比较有用
        
except Exception,e:
    print '记录登录信息到日志'
    print e



######################面向对象实验题#################################
class Persion(object):
    def __init__(self,name,weight):
        self.Name = name
        self.Weight = weight
        self.Age = None
        
    def talk(self,content):
        print self.Name,'said',content
        
    def fight(self,value):
        if self.Weight > value:
            print 'go'
        else:
            print 'run'
            
p1 = Persion('jack',150)
p1.Age = 26
p2 = Persion('tom',100)

p1.talk('i am p1')
p2.talk('i am p2')

p1.fight(p2.Weight)

print p1.__dict__   #可以打印出p1的所有属性
print p2.__dict__
print dir(p2)    #可以打印出更多的属性，包含自带的__init__,__dict__,__doc__,__module__
print p2.__dict__.get('Name')







