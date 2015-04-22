#! /usr/bin/env python
#_*_ coding:utf-8 _*_
from multiprocessing import Process, Manager


def f(d, l, k, i):
    d[111] = 'no.1'       #dict指明key的值是数字
    d['2'] = 2222         #dict指明key的值是字符串
    d[2222] = 'LLLLLLL'   #dict指明key的值是数字
    d[0.25] = None        #dict指明key的值是数字
    d[i] = i
    l.reverse()           #反转列表，在本例中反转了多次
    k.append(i)

if __name__ == '__main__':
    manager = Manager()

    d = manager.dict()
    #定义了一个空字典
    l = manager.list(range(10))
    #定义了一个列表
    k = manager.list()
    
    for i in range(21):
        p = Process(target=f, args=(d, l, k, i))
        p.start()
        p.join()

    print d
    print l
    print k
    
#     dd = (str(d))
#     
#     with open('E:/tmp.txt','wb') as hh:
# 
#         hh.write(dd)
        
#         data = hh.readlines()
#         print data
    
#     with open("E:\tmp.txt"'", 'r') as f2
#         print f2.readlines()   
    
#可以将数据，字典，列表做为进程共享的数据，manager是经过特殊处理的
    