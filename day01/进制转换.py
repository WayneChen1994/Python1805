#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Wayne.Chen


 # 十进制转为二进制
print(bin(4))   # 0b100
print('{0:b}'.format(4))    # 100

# 十进制转为八进制
print(oct(8))   # 0o10
print('{0:o}'.format(8))    # 10

#十进制转为十六进制
print(hex(15))  # 0xf
print('{0:x}'.format(15))   #f

# 通过int函数，可以将二进制、八进制或者十六进制的字符串转为十进制的数值
'''
语法：
int('需要转换的字符串', 指定进制)
'''
# print(int('10', 16))
print(eval('0b1010'))
print(eval('0o10'))
print(eval('0x10'))
print('{0:d}'.format(0b1010))
# 中国 = 'china'
# print(中国)
a = 10
a1 = 20
# 1a = 30
