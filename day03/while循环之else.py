#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
在while循环中存在一个else语句
语法：
while 条件判断:
    语句块1
else:
    语句块2
else语句执行的条件，当正常跳出循环体的时候
【正常循环结束的时候】，会执行else语句
非正常结束：break
'''


'''
判断输入的银行卡密码【6位】0~9是否合法
'''


# n = 1
# res = 0
# while n <= 10:
#     res += n
#     n += 1
#     if n % 9 == 0:
#         break
# else:
#     print("res =", res)


'''
语句组：
当while循环后面只有一条语句的时候，我们可以将该语句与while语句强制性写成一行
'''


# while True: print("hello")
