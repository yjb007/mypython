#! /usr/bin/env python
#_*_ coding:utf-8 _*_

#生产者消费者模型，三个角色
#生产者，消费者，队列
#
from threading import Thread
from Queue import Queue
import time

class Producer(Thread):
#创建生产者类
    
    def __init__(self,name,queue):
           
        self.__Name = name
        self.__Queue = queue
        #name,生产者的名称;queue,队列容器
        super(Producer,self).__init__()
        #执行一下父类的构造函数
    def run(self):
        while True:
            if self.__Queue.full():
                time.sleep(10)
                #如果queue队列满了，则休息一秒
            else:
                self.__Queue.put('包子')
                print que.qsize()
#                 time.sleep(1)
                print '%s 生产了一个包子子子子子子子子子子子子子子子子子' "\n" %(self.__Name) 
                #没满的话则休息5秒再往里面放包子，可能一下子就把队列放满了
#         Thread.run(self)
        

class Consumer(Thread):
    
    def __init__(self,name,queue):
    
        self.__Name = name
        self.__Queue = queue
        #name,消费者的名称;queue,队列容器
        super(Consumer,self).__init__()
        #执行一下父类的构造函数
        
    def run(self):
        while True:
            if self.__Queue.empty():
                time.sleep(10)
                #如果队列空了，没包子了，则休息一秒
            else:
                self.__Queue.get()
                print que.qsize()
#                 time.sleep(1)
                #运行time.sleep(1)会释放线程
                print '%s 消费了一个包子' "\n" %(self.__Name)
                #队列没空的话则拿包子，并打印出这次循环线程使用的哪个消费者来拿包子
#         Thread.run(self)
        
que = Queue(maxsize=100)
#实例化Queue创建一个对象，队列长度最大是100

Producer01 = Producer('生产者01',que)
Producer02 = Producer('生产者02',que)
Producer03 = Producer('生产者03',que)
Producer01.start()
Producer02.start()
Producer03.start()

for item in range(20):
    name = '消费者%s' %(item,)
    temp = Consumer(name, que)
    temp.start()

#单线程python，主线程顺序执行，Producer01，Producer02，Producer03，Consumer[1-20].start()，到代码最后退出
#由于其中的Producer01，Producer02，Producer03，Consumer[1-20].start()函数中包含了死循环
#因此子线程Producer01，Producer02，Producer03，Consumer[1-20].start()会轮流一直顺序执行下去，没有顺序，谁抢到资源就执行谁的










'''
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
'''
