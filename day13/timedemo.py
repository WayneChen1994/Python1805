#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author：zhangjiao
import  time

'''
将封装的time模块改写成一个类，继承于time模块
'''


class MyTime(time):
    def __init__(self):
        super(MyTime, self).__init__()

    def getstrtime(self, t1=time.time()):
        lt = self.localtime(t1)
        return self.strftime("%Y-%m-%d %X",lt)

    def strttotime(self, strtime):
        st = self.strptime(strtime,"%Y-%m-%d %X")
        return self.mktime(st)


if __name__ == "__main__":
    mt = MyTime()
    print(mt.getstrtime())
