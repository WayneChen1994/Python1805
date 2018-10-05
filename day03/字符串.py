#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author: Wayne.Chen


'''
字符串：使用单引号或者双引号括起来的任意长度的任意字符，我们称之为字符串
定义字符串：
变量名 = ""/''
'''

# str1 = "hello"
# str2 = "world"

'''
字符串拼接
1、方法1，通过“+”
注意：不同类型的不能进行相加
2、使用“,”来进行拼接
注意：在“,”的地方会产生一个空格
3、使用格式化输出
注意：使用格式化输出字符串的时候，占位符要使用%s
4、str1.join(序列)
作用：使用指定的字符串str1将序列中的字符串进行拼接，返回一个新的字符串

重复输出字符串
str1*n
作用：重复输出n次str1
'''

# str3 = str1 + str2
# print(str3)
# # str4 = str3 + 20
# # print(str4)
# print(str2, str3)
# print("%s%s" % (str2, str3))
# list1 = ["hello", "good", "nice"]
# print("&&".join(list1))
# print("&&".join("hello"))
# print("*"*50)

'''
获取字符串中的指定字符
通过下标来进行获取的
注意：下标是从0开始数的【从左边开始取】。
str[下标]
也可以从右边开始取值，下标是从-1开始的
-1代表倒数第一个字符
注意：下标有时候也称索引index
'''
# str1 = "nihao"
# print(str1[4])
# print(str1[-1])

'''
字符串的截取
str[start:end]
取值区间[start,end)
当start不写，默认从0开始取
当end不写，默认取到最后
当start和end都不写，默认取全部
'''
str2 = "you are a good man"
print(str2[4:7])
print(str2[:7])
print(str2[4:])
print(str2[:])

print('a' not in str2)

'''
格式化输出：
1、输出字符串使用%s
2、输出浮点数使用%f
3、输出int类型使用%d
4、保留两位小数：%.2f
5、指定输出的宽度：%2d
6、指定输出字符串左对齐%-2d
'''
print("%02d:%-2d:%-2d"% (17, 0, 9))




