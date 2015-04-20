#! /usr/bin/env python
#_*_ coding:utf-8 _*_

#生产者消费者模型，三个角色
#生产者，消费者，队列
#
from threading import Thread
from Queue import Queue

class Producer(Thread):
    
    def __init__(self,name,queue):
    
        self.__Name = name
        self.__Queue = queue
        #生产者的名称和队列
        
    def run(self):
        self.__Queue.put('包子1')
        Thread.run(self)
        

class Consumer(Thread):
    
    def __init__(self,name,queue):
    
        self.__Name = name
        self.__Queue = queue
        #生产者的名称和队列
        
    def run(self):
        self.__Queue.get()
        Thread.run(self)
        
que = Queue(maxsize=100)
#队列是先进先出，线程安全
#生产者往队列放，消费者从里面取

print que.qsize()

que.put('1')
que.put('2')
que.put('3')
que.put('4')
que.put('5')
#往队列里存放了5条数据

print que.qsize()
#查看队列的大小，数据多少

print 'empty:',que.empty()
#查看队列是否是空
print 'get', que.get()
print 'get', que.get()
print 'get', que.get()
print 'get', que.get()
print 'get', que.get()
# print 'get', que.get()
#取出数据，先进先出取数据
#如果队列为空，再执行去操作，则会阻塞

print 'empty:',que.empty()

