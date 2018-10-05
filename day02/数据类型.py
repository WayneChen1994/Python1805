#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:Wayne.Chen

# int1 = 100
# int2 = -10
# 使用type可以查看变量的类型
# print(type(int1))
# print(type(int2))
# float1 = 12.345
# float2 = 10 / 3
# print(type(float1))
# print(float1)
# print(float2)
num = 12+6j
# print(type(num))

# str1 = 'hello world'
# str2 = "you are great"
# I'm fine
# I'm "OK"
# str3 = "I'm fine"
# str4 = 'I\'m \"OK\"'
# print(type(str1))
# print(type(str2))
# print(str3)
# print(str4)

'''
基本数据类型：
1、number类型
a、整数,分为正整数与负整数，在Python中的表示方式与数学中相同
b、浮点数【小数】，可能会出现一定的误差
c、复数

2、字符串：以单引号或者双引号括起来的任意文本
int,float,str   内置函数，【避免使用内置函数的函数名来命名变量】

转义字符：\
在字符串中，有很多转义字符，常见的\" ==> "
\' ==> '    \n ==> 换行   \t ==> 制表符  \\ ==> \
\r ==> 光标移到下一行

三引号，当内容比较多的情况下，需要换行的时候我们可以使用此方法

3、布尔值
只有两个取值，True或者False【注意大小写】

4、None（空值）
它的取值是一个特殊值，与0并不相同，注意大小学

5、list（列表）
list是一个有序的集合

6、tuple（元组）
tuple也是一个有序的集合，一旦初始化就不能修改

7、dict（字典）
以键值对的方式存储，对于其键：1、不能重复 2、不可变类型
优点：查找速度极快
缺点：占用内存比较大

8、set集合
它只存储了字典中的Key，存储的数据的特点：
1、不能重复
2、元素为不可变类型

不可变类型：
number、str、tuple、bool、None
可变类型
list、dict、set
'''

# 10\5=2
# num1 = 10
# num2 = 5
# print("%d\\%d=%d" % (num1, num2, num1/num2))
# print(str(num1)+"\\"+str(num2)+"="+str(int(num1/num2)))

# print("line1\nline2\nline3")
# print('''line1
# line2
# line3''')

# bool1 = True
# bool2 = False
# print(bool1)
# print(bool2)

num2 = None
num3 = 0
# print(num2 == num3)

list1 = [1,2,3,True,False,"hello",[1,2,3]]
print(list1)
tuple1 = (1,2,3,True,False,"hello",[1,2])
print(tuple1)

dict1 = {"name":"lili","age":18}
set1 = {"name", "age"}
print(type(dict1))
print(type(set1))









