#! /usr/bin/env python
#_*_ coding:utf-8 _*_

from multiprocessing import Pool
import time
import threading

def t_func(li,n):
    print 'thread:',n
    
def f(x):
    info_list = []
    for i in range(5):
        t = threading.Thread(target=t_func, args=(info_list,i))
        t.start()

#多进程里面多线程
pool = Pool(processes=4)
#同时在CPU上运行的进程是在这里定义的，这里是同时运行4个
#进程的运行也是有优先级的，进程太多可能产生僵尸进程
res_list = []
if __name__ == '__main__':
    for i in range(10):
        res = pool.apply_async(f, [i,])
        #res = Process(target=f,args=[i,])
#         res.get()
        res_list.append(res)
        
for r in res_list:
        print r.get(timeout=1)

print pool.map(f,range(10))
#此方法只能在linux下执行
#这个地方的r.get()需要和pool.apply_async(f, [i,])配合使用
#这个写法不常用，但要知道
