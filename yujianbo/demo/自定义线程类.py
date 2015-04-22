#! /usr/bin/env python
#_*_ coding:utf-8 _*_

from threading import Thread
import time

class MyThread(Thread):
#自定义一个MyThread类，继承Thread，子类不能访问父类的私有方法和私有字段  
    def run(self):
        time.sleep(1)
        print 'change thread run method'
        Thread.run(self)
        #直接调用父类的方法
def Bar():
    print 'ttt'

t1 = MyThread(target=Bar)
t1.start()
#t1.start()会运行MyThread的run方法，所以Bar()的'ttt'永远不会被打印出来
print 'end'
#主线程会一直往下执行，但是会等待子线程运行完毕，正常不加参数的情况


#多线程执行流程