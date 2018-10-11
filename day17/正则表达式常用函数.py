#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import re


str1 = "123 wewe 133 efr 212 123"
print(re.findall("123", str1))
print(str1.find("123"))


# 工具类
'''
re.compile(pattern, flags)
参数一：正则表达式
参数二：标志位
功能：返回一个正则表达式的对象，在正则对象的时候，使用此对象即可
'''


def getMailCompile():
    return re.compile(r'([1-9]\d{4,11}@qq.com$)|(\w{5,12}@(163.com|sina.cn)$)')


print(getMailCompile().match("12345@sina.cn"))
print(getMailCompile().match("12345qq@sina.cn"))


'''
re.match(pattern, string, flags)
参数一：正则表达式
参数二：被正则的字符串
参数三：标志位
功能：从字符串的开始进行匹配，若匹配成功则返回一个对象，
若匹配不成功则返回None
【注意：它是从字符串的开始进行匹配的，它并不是一个完全匹配，
若字符串没有匹配结束，但是已经找到匹配的对象，这也算是匹配成功，
若想完全匹配，需要在正则表达式的末尾添加边界值$】
'''


'''
re.search(pattern, string, flags)
参数一：正则表达式
参数二：被正则的字符串
参数三：标志位
功能：按照正则表达式在整个字符串中进行查找，若找到一个则不继续查找，
而是立即返回匹配对象，若整个字符串都没查询到，则返回None
'''


print(re.search("123", str1))
print(re.search("123a", str1))


'''
re.findall(pattern, string, flags)
参数一：正则表达式
参数二：被正则的字符串
参数三：标志位
功能：查询字符串中所有符合正则表达式的子串，并且以列表的形式返回，
若没找到则返回一个空列表

re.finditer(pattern, string, flags)
与findall效果相同，只不过返回的是一个迭代器
'''


str2 = "hello Hello HEllo"
print(re.findall("123", str1))
print(re.findall("hello", str2, flags=re.I))
iterobj = re.finditer("hello", str2, flags=re.I)
print(next(iterobj))


'''
re.split(pattern, string, maxsplit, flags)
参数一：正则表达式
参数二：被正则的字符串
参数三：最大分割次数
参数四：标志位
功能：将指定的字符串按照正则表达式来进行切割，
切割的字符串不保留【与字符串的切割相同】
若指定的最大分割的次数大于实际能够分割的次数，也不报错，
分割的次数以实际能够分割次数为准
'''
print(re.split("h", str2, flags=re.I))


'''
需求：以数字进行切片
'''


str3 = "123 sdo3iife 345 dwefrpoe 5677nfdrg90ftyt"
print(re.split(r'\d+', str3, maxsplit=2))


'''
需求：将连续的数字替换***
'''


'''
re.sub(pattern, repl, string, count, flags)
参数一：正则表达式
参数二：要替换的字符串（也可以是函数）
参数三：被正则的字符串
参数四：指定替换的次数
参数五：标志位
功能：在指定的string中，使用pattern进行匹配到的字符串使用repl进行
代替，可以使用count指定替代的次数，若替换的次数大于实际能够替换的次数，
则以实际能够替换的次数为准，并且将新串返回。
'''


print(re.sub(r'\d+', '***', str3, count=3))
