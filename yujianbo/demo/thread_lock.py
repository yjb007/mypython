#! /usr/bin/env python
#_*_ coding:utf-8 _*_
import time
import threading

lock = threading.Lock()
#线程锁
num = 0
def run(n):
    global num
    #global可以让局部变量可以修改全局变量，不建议使用
    time.sleep(1)
    
    samp.acquire()
    num +=1
    print '%s\n' %num
    samp.release()



samp = threading.BoundedSemaphore(4)
#代替lock.acquire()，设置 最大同时执行的数量，用在设置mysql的最大连接数
for item in range(100):
    t = threading.Thread(target=run,args=(item,))
    t.start()
#启用100个线程，被全局解释器锁限制，只有一个被执行


#print时会去抢屏幕输出  

    