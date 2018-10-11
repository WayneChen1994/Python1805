#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import re


'''
尽可能多的匹配，我们称之为贪婪匹配
x*  匹配0个或者任意多个x
x+  匹配至少1个x
x{n,}   匹配至少n个
x{n,m} 匹配n到m个x【最多匹配m个，n<m】
注意：以上这几个都是尽可能多地匹配
'''


'''
x?  匹配0个或者1个x 【非贪婪匹配】
一般情况下用来限制贪婪匹配。
通常情况下?都与贪婪匹配一起使用。
'''


r'''
在正则中具有特殊意义的标点符号：
. [] () ? * + \ | {} ^ $
若匹配这些标点符号的时候，需要添加\
.*?:代表匹配任意多个任意字符
'''


print(re.findall(r'a*', "aaabbbaaaaccccaaaaa"))
print(re.findall(r'a', "aaabbbaaaaccccaaaaa"))


'''
1、需求，提取字符串中的数字
'''


str1 = "12wndskd23467fh0099"
str2 = "lili28leilei32haha22"
str3 = "lili50leilei100haha8000"
str4 = "lili5000leilei100000haha8000000"
print(re.findall(r'\d', str1))
print(re.findall(r'\d+', str2))
print(re.findall(r'\d{3,}', str3))
print(re.findall(r'\d{3,6}', str4))


str5 = "you are good man,you are a great man,you are a nice man"


'''
需求：将字符串中所有you...man提取出来。
'''


print(re.findall(r'you.*?man', str5))


str6 = "/* hello */ /* world */ /* 你好 */"


'''
需求：提取/*...*/
'''
print(re.findall(r'/\*.*?\*/', str6))


str7 = "\.? hello \.? \.? nice \.? \.? good \.?"


'''
提取：.? ... .?
'''
list1 = re.findall(r'\\\.\?.*?\\\.\?', str7)
print(list1[0])


'''
判断邮箱地址是否合法：
xxxx@qq.com [5~12]
xxxx@163.com [数字字母下划线]
xxxx@sina.cn
'''


print(re.match("[1-9]\d{4,11}(@qq.com|@163.com|@sina.cn)$", "1234@qq.com"))
print(re.match("[1-9]\d{4,11}(@qq.com|@163.com|@sina.cn)$", "12345@qq.com"))
print(re.match("[1-9]\d{4,11}(@qq.com|@163.com|@sina.cn)$", "12345@sina.com"))
print(re.match("[1-9]\d{4,11}(@qq.com|@163.com|@sina.cn)$", "12345@sina.cn"))
print(re.match("[1-9]\d{4,11}(@qq.com|@163.com|@sina.cn)$", "12345w@163.com"))


print(re.match(r'([1-9]\d{4,11}@qq.com$)|(\w{5,12}@(163.com|sina.cn)$)', "12345ws@163.com"))
print(re.match(r'([1-9]\d{4,11}@qq.com$)|(\w{5,12}@(163.com|sina.cn)$)', "12345ws@qq.com"))
print(re.match(r'([1-9]\d{4,11}@qq.com$)|(\w{5,12}@(163.com|sina.cn)$)', "12345678@qq.com"))
