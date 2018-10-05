'''
获取当前时间的下一秒

import time
nowTime = time.strftime("%H:%M:%S", time.localtime(time.time()))
timeList = nowTime.split(":")
h = int(timeList[0])
m = int(timeList[1])
s = int(timeList[2])
s += 1
if s == 60:
    m += 1
    s = 0
    if m == 60:
        h += 1
        m = 0
        if h == 24:
            h = 0
print("时间下一秒：%02d:%02d:%02d" % (h,m,s))
'''

'''
阶乘与循环求n!
def jianchengDG(n):
    if n == 1:
        return 1
    else:
        return jianchengDG(n - 1) * n


def jianchengXH(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


import time

startTimeDG = time.clock()
print(jianchengDG(998))
endTimeDG = time.clock()
print("递归耗时：%f" % (endTimeDG - startTimeDG))

startTimeXH = time.clock()
print(jianchengXH(998))
endTimeXH = time.clock()
print("循环耗时：%f" % (endTimeXH - startTimeXH))
'''