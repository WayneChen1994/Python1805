#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


print()


'''
str1.count(str2[,start][,end])
功能：返回str2在str1中出现的次数
start：若不写，默认为0
end：若不写，默认为len(str)-1
若不指定start和end则查找的是整个字符串
'''


str1 = "you are very good,you are very great!!"
print(str1.count("you"))
print(str1.count("you",0,18))


'''
str1.find(str2[,start][,end])
从左到右开始查找
功能:返回str2在str1中出现的第一个下标值，
若没有找到则返回-1
使用start和end可以指定查询范围，若不写，则默认整个字符串
'''


print(str1.find("you"))
print(str1.find("you",1,18))


'''
str1.rfind(str2[,start][,end])
功能：从右到左进行查找，返回str2在str1出现的第一个下标值，若找不到则返回-1
'''


print(str1.rfind("you"))
print(str1.rfind("you",1,18))


'''
str1.index(str2[,start][,end])
功能：与find相同，只不过当str2不存在的时候不会返回-1
取而代之报错ValueError

str1.rindex(str2[,start][,end])
功能：与rfind相同，不同在于当str2不存在的时候rfind返回-1，
rindex报错ValueError
'''


# print("*"*50)
# print(str1.index("you"))
# print(str1.index("you",1,18))
# print("*"*50)
# print(str1.rindex("you"))
# print(str1.rindex("you",1,18))


str3 = "hello"
str4 = "**hello**"
print(str3)
print(str4)


r'''
str1.lstrip([chars])
功能：截掉str1左边指定的字符串chars，并且返回一个新串
若参数不写，则默认去掉空白字符【\r \n \t " "】

str1.rstrip([chars])
功能：截掉str1右边指定的字符串chars，并且返回一个新串
若参数不写，则默认去掉空白字符【\r \n \t " "】

str1.strip([chars])
功能：截掉str1两边指定的字符串chars，并且返回一个新串
若参数不写，则默认去掉空白字符【\r \n \t " "】
'''


print(str4.lstrip("*").rstrip("*"))
print(str4.strip("*"))
print("*"*50)


'''
str1.split([str2][maxsplit=num])
参数一：指定切割字符串【可不写，默认使用空白符】
参数二：指定切割的次数【可不写，默认为-1，全部切割】
注意：当num大于字符串本身能够切割的次数的时候，则忽略，
若num小于能够切割的次数，则切割num次
功能：返回从左往右进行切割，以指定字符串str2切割str1，切割后的字符串为元素组成的一个列表【不保留指定的字符串】

str1.rsplit([str2][maxsplit=num])
参数一：指定切割字符串【可不写，默认使用空白符】
参数二：指定切割的次数【可不写，默认为-1，全部切割】
注意：当num大于字符串本身能够切割的次数的时候，则忽略，
若num小于能够切割的次数，则切割num次
功能：返回从右往左进行切割，以指定字符串str2切割str1，切割后的字符串为元素组成的一个列表【不保留指定的字符串】
'''


print(str1.split(maxsplit=2))
print(str1.rsplit(maxsplit=2))


'''
str2.splitlines()
功能：以行来进行分割str2，并返回切割后的列表
'''


str2 = '''row1 abs
row2 qwerty
row3 sda fdsf'''
print(str2.splitlines())
