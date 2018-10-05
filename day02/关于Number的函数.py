#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Wayne.Chen

print(int(12.34))
# print(int(12.84))
# print(int("12"))
# print(int("+12"))
# print(int("-12"))
# print(int("1+2"))
# print(int("12+"))
# print(int("12-"))
# print(float(12))
# print(float('12.34'))
# print(float('12'))
# print(float('+12.23'))
# print(float('-12.23'))
# print(float('12.2+3'))
# print(float('12.2-3'))

'''
int()函数能够将float类型转为int类型（向下取整）
也能够将有效的字符串类型转为int类型

float()函数能够将int类型转为float类型
也能够将有效的字符串类型转为float类型

abs()   返回数值的绝对值
max(num1,num2,……,numn)  返回数值中最小值
min(num1,num2,……,numn)  返回数值中最小值
注意：当只有一个参数时，参数必须为可迭代类型

pow(x, y)   返回x的y次方

round(x, n=0)   返回浮点数的四舍五入值，n为保留的小数位数
在3.x版本中若小数出现5的时候，则得到的结果向偶数靠拢
如：print(round(12.5)) ==> 12
    print(round(13.5)) ==> 14
'''

# age = int(input("请输入您的年龄："))
# age = age + 1
# print(age)

# print(abs(12))
# print(abs(-12))
# print(12>13)
# print(max(1,2,3,43,5,6))
# print(min(1,2,3,43,5,6))
# print(max(1,2))
# print(min(1,2))
# print(max([1]))
# print(min(2))

print(pow(2,3))
print(round(12.34, 1))
print(round(12.56898, 3))
print(round(12.5))
print(round(13.5))
