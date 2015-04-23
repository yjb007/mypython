#! /usr/bin/env python
#_*_ coding:utf-8 _*_


from multiprocessing import Pool
from multiprocessing import Process
import threading
import time
import os

def f(item):
#     for item in xrange(1000):
        return item*item


a = [1,2,3,4,5,6,7,8,9]

if __name__ == '__main__':
    p = Pool(2)
    print p.map(f, a)
#多进程使用方法1  




def Foo(i):
    print 'say hello, %s'  %i
    print 'module name:', __name__
    if hasattr(os, 'getppid'):
        print 'parent process:', os.getppid() 
        # only available on Unix,在windows上调试无效
    print 'process id:', os.getpid()
    
def Foo2(name):
    Foo('Call function Foo Later')
    print 'hello', name


if __name__ == '__main__':
    Foo('print Function First')
    for i in range(10):
        p = Process(target=Foo2,args=(i,))
        p.start()
        p.join()
        #p.join()会让进程串行，有wait的意思


#多进程使用方法2
#进程调用另外一个进程，fork出一个子进程，系统会复制一份完全相同的内存给子进程使用
    
    
    