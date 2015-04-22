#! /usr/bin/env python
#_*_ coding:utf-8 _*_

import threading
import time

event = threading.Event()

def Producer():
    print '等人来买包子中。。。'
    event.wait()
    #等待将标志位flag为设置为true，不然会一直等待
    event.clear()
    #将标志位flag为归位为false
    
    print "有人来买包子了"
    
    print '开始做包子。。。'
    
    time.sleep(5)

  
    event.set()     
    print '包子做好了，快来拿'
    


def Consumer():
    print '我是客户，我要去买包子了'
    event.set()
    #设置标志位flag为true,默认是false
    
    time.sleep(2)
    print '等待老板做包子中。。。。'
    while True:
        if event.isSet():
            print '谢谢老板'
            break
        else:
            print '这么慢，还没好啊？！！'
            time.sleep(1)
    

p = threading.Thread(target=Producer)
c = threading.Thread(target=Consumer)

p.start()
c.start()
#启动多个线程，可以通过que来做线程数的启动

##异步模型，单线程实现


#对于python的伪多线程实际是单线程
#但在处理IO密集型时，因为硬盘速度慢，所以可以在处理磁盘IO时，可以先行处理别的线程
#多线程一定要加lock，因为数据出问题，event,处理好线程间的关系





    