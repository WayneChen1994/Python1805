#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
str1.isdigit()
str1.isdecimal()
功能：判断字符串str1是否只是由数字组成，若是则返回True，否则返回False
'''


str1 = "12323"
str2 = "一二三"
str3 = "I II III"


print(str1.isdigit())
print(str1.isnumeric())
print(str1.isdecimal())
print("*" * 50)
print(str2.isdigit())
print(str2.isnumeric())
print(str2.isdecimal())
print("*" * 50)
print(str3.isdigit())
print(str3.isnumeric())
print(str3.isdecimal())


'''
str.isspace()
功能：判断字符串中是否只包含空白符，若是则返回True，否则返回False
'''


print(" ".isspace())
print(" \n".isspace())
print(" \t".isspace())
print(" \r".isspace())
print("11 1".isspace())


print(ord("A"))
print(ord("a"))
print(ord("中"))


print(chr(97))
print(chr(20014))
print(chr(20012))
print(chr(20190))
