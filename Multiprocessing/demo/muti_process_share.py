#! /usr/bin/env python
#_*_ coding:utf-8 _*_

from multiprocessing import Process
from multiprocessing import Queue
#这个Queue和直接导入的 import Queue不是一回事
#这个Queue是经过封装的，多个进程会共享者一个Queue

def ff(q,n):
    q.put([n, 'hello'])

if __name__ == '__main__':
    q = Queue()

    for i in range(5):
        p = Process(target=ff, args=(q,i))
        p.start()
    
    while True:
        print q.get()

     
        
#可以使用队列让多个进程共享一份数据，q是队列，因为q队列是单独声明的，所以只有一个q队列













