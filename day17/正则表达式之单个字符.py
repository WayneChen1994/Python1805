#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
若使用正则表达式的时候，我们首先要先导入re模块
'''


import re


'''
匹配单个字符
.   匹配除换行符以外的任意字符
[]  匹配方括号中的任意一个字符
[0-9]   匹配所有的数字
[a-z]   匹配所有的小写字母
[A-Z]   匹配所有的大写字母
[a-zA-Z]匹配所有的之字母
[a-zA-Z0-9_]匹配所有的数字字母下划线
[^0-9]  匹配所有的非数字字符，【^脱字符，表示不匹配】
\d      效果等同于[0-9]
\D      效果等同于[^0-9]
\w      效果等同于[a-zA-Z0-9_]
\W      效果等同于[^a-zA-Z0-9_]
\s      匹配所有的空白符，效果等同于[ \n\t\r\f]
\S      匹配所有非空白符，效果等同于[^ \n\t\r\f]
'''


print(re.findall(".", "1233\n"))
print(re.findall("[1234]", "hello1,2world5"))
print(re.findall("[good]", "hello1,2world5"))
# 匹配所有的数字
print(re.findall("[0-9]", "hello1,2world5"))
print(re.findall("\d", "hello1,2world5"))
print(re.findall("\D", "hello1,2world5"))
print(re.findall("\D", "hello1,2world5"))
# 匹配所有小写的字母
print(re.findall("[a-z]", "hello1,2WorlD5"))
# 匹配所有大写的字母
print(re.findall("[A-Z]", "hello1,2WorlD5"))
# 匹配所有字母【包括大写和小写】
print(re.findall("[a-zA-Z]", "hello1,2WorlD5"))
# 匹配所有的数字、字母、下划线
print(re.findall("[0-9a-zA-Z_]", "hello1_,2WorlD5"))
print(re.findall("\w", "hello1_,2WorlD5"))
print(re.findall("\W", "hello1_,2WorlD5"))
print(re.findall("[^0-9a-zA-Z_]", "hello1_,2WorlD5"))
# 匹配所有非数字字符
print(re.findall("[^0-9]", "hello1_,2WorlD5"))
# 匹配空白符
print(re.findall("\s", " \n\f"))
# 匹配非空白符
print(re.findall("\S", "aa \n\f"))


'''
需求：匹配以任意字符开头，第二位为数字
'''


print(re.findall(".\d", "12hello334"))


'''
需求：从字符串中提取5位的QQ号码
'''

print(re.findall(r'[1-9]\d\d\d\d', 'ewq043255rewrst654653fsgg'))
