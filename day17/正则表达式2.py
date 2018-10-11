#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import re


r'''
^   行首匹配 【受re.M模式影响，若re.M的模式下，匹配字符串的每一行的行首】
$   行尾匹配 【受re.M模式影响，若re.M的模式下，匹配字符串的每一行的行尾】
x{n}表示匹配连续的n个x字符
\A  匹配字符串的开始，功能类似于^，它不受re.M模式的影响
\Z  匹配字符串的结束，功能类似于$，它不受re.M模式的影响

\b  匹配单词的边界，当\b写在单词左边，表示匹配左边界，
当\b写在单词右边，表示匹配右边界，
当\b同时出现在单词两边，则表示匹配整个单词

注意：\b是一个转义字符，使用的时候前面加r，不让字符串转义

\B  匹配非单词边界
当\B写在单词左边，表示不匹配左边界
当\B写在单词右边，表示不匹配右边界
当\B写在单词两边，表示不匹配左右边界
  
注意：使用的时候，一般^与$一起连用，\A与\Z一起连用
^与\A一定要写在正则表达式的最前面，$与\Z一定要写在正则表达式的结尾
'''


'''
判断是否是5位合法的QQ号
'''
print(re.findall(r'^[1-9]\d\d\d\d', '432556rewrst654653fsg67'))
print(re.findall(r'^[1-9]\d\d\d\d$', '432556rewrst654653fsg67'))
print(re.findall(r'^[1-9]\d\d\d\d$', '432556432561'))
print(re.findall(r'^[1-9]\d\d\d\d$', '4311'))
print(re.findall(r'^[1-9]\d\d\d\d$', '43115'))


'''
判断11位的电话号码是否合法
'''
print(re.findall(r'^1\d\d\d\d\d\d\d\d\d\d$', '18927106340'))
print(re.findall(r'^1\d\d\d\d\d\d\d\d\d\d$', '28927106340'))
print(re.findall(r'^1\d\d\d\d\d\d\d\d\d\d$', '1892b10a340'))
print(re.findall(r'^1\d\d\d\d\d\d\d\d\d\d$', '189271063401'))


print(re.findall(r'^1\d{10}$', '18927106340'))
print(re.findall(r'^1\d{10}$', '28927106340'))
print(re.findall(r'^1\d{10}$', '189b710a340'))
print(re.findall(r'^1\d{10}$', '189271063401'))


'''
需求：提取字符串中的6个6
'''


print(re.findall(r'6{6}', 'rewt66666rwgdsfs6666666gsgdhgsfds2342566632rse666666'))


str1 = '''12345
67890
54321
'''


print(re.findall('^\d{5}$', str1))
print(re.findall('^\d{5}$', str1, flags=re.M))
print(re.findall('\A\d{5}$', str1, flags=re.M))
print(re.findall('\A\d{5}\Z', str1, flags=re.M))


print(re.findall(r'er\b','erverer'))
print(re.findall(r'\ber','erverer'))
print(re.findall(r'\ber\b','erverer er'))


print(re.findall(r'er\B','erverer'))
print(re.findall(r'\Ber','erverer'))
print(re.findall(r'\Ber\B','erverer er'))
