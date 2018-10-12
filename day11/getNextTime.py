#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import time


# 获取当前时间的下一秒
def getNextSecond():
    currentTimeStr = time.strftime('%X', time.localtime())
    timeList = currentTimeStr.split(':')
    h = int(timeList[0])
    m = int(timeList[1])
    s = int(timeList[2])
    s += 1
    if s == 60:
        s = 0
        m += 1
        if m == 60:
            m = 0
            h += 1
            if h == 24:
                h = 0
    return '%02d:%02d:%02d' % (h, m, s)


if __name__ == '__main__':
    print(getNextSecond())
