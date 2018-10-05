#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author: Wayne.Chen


'''
break语句
作用：跳出当前循环体，结束循环

continue语句：
作用：结束本次循环，继续下一次【没有跳出循环体】
注意：continue下面的代码不再执行

pass语句：
作用：本身没有任何含义，保证语义的完整性
'''

'''
需求：1+2+……+100的值
当用户输入n，若n<100，则返回1+2+……+n的值；
若n >= 100，返回1+2+……+100的值
'''

# n = int(input("请输入一个整数："))
# res = 0
# num = 1
# while num <= 100:
#     if num <= n:
#         res += num
#     else:
#         break
#     num += 1
# print(res)

'''
需求2：
求0+2+4+8+……+100的和
'''

# sum = 0
# num = 0
# while num <= 100:
#     num += 1
#     if num % 2 == 0:
#         sum += num
#     else:
#         continue
# print(sum)

# res = 0
# n = 0
# while n <= 100:
#     res += n
#     n += 2
# print(res)




