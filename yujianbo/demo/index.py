#! /usr/bin/env python
#_*_ coding:utf-8 _*_
import time
from threading import Thread
#threading.Thread模块，类

def Foo(arg1,arg2):
#     print arg1, "\n", arg2
    for item in range(10):
        print item
        time.sleep(1)

t1 = Thread(target=Foo,args=(111,222,))
t2 = Thread(target=Foo,args=(111,222,))
print t1.getName()
print t2.getName()
#实例化创建一个对象，通过构造函数创建
#创建的线程对象调用函数Foo
t1.setDaemon(True)
t2.setDaemon(True)
#设置子线程t1和t2为守护线程： 如果主线程不结束，则会继续执行，主线程结束，则停止执行，执行到哪是哪
#同时主线程会依然一直往下走

t1.start()
t2.start()
#主线程会一直往下走，不会等待中间创建的进程t1和t2，即使主线程结束，子线程t1和t2依然会继续执行
#中间创建的线程t1和t2不会互相阻塞，会同时运行
t1.join()
t2.join(4)
#会让主线程等到到子线程运行完毕后，主线程再继续运行
#t2.join(4)会等到4秒

print 'end'
print 'end'
print 'end'
time.sleep(6)
#会导致线程停止运行

