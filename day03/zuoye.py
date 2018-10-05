#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author: Wayne.Chen


'''
求出200到500之间奇数+能被7整除的个数
count = 0
for x in range(200, 501)[1::2][1::7]:
    count += 1
print(count)
'''

'''
百钱买百鸡
'''

for i in range(1, 20):
    for j in range(1, 33):
        k = 100 - i - j
        if k % 3 == 0 and i*5+j*3+k/3 == 100:
            print("公鸡：%d只，母鸡：%d，小鸡：%d" % (i, j ,k))





