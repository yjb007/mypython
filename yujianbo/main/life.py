#! /usr/bin/env python
#_*_ coding:utf-8 _*_
class Persion(object):
    def __init__(self,name,weight):
        self.Name = name
        self.Weight = weight
        self.Age = None
        
    def talk(self,content):
        print self.Name,'said',content
        
    def fight(self,value):
        if self.Weight > value:
            print 'go'
        else:
            print 'run'
            
p1 = Persion('jack',150)
p1.Age = 26
p2 = Persion('tom',100)

p1.talk('i am p1')
p2.talk('i am p2')

p1.fight(p2.Weight)

