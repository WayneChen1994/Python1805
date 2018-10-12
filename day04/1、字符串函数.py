#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


print()


'''
1、eval(str)
功能：能将str转成有效表达式【Number类型，list、tuple、set】
并且返回计算结果，当无法转换的时候则报错
'''


# print(eval("123"))
# print(eval("+123"))
# print(eval("-123"))
# print(eval("12+3"))
# print(eval("12-3.7"))
# print(eval("12.05-3"))
# list1 = eval("[1,2,3,4]")
# tuple1 = eval("(1,2,3,4)")
# print(type(list1))
# print(type(tuple1))


'''
2、str()函数，可以将任意类型的数据转为字符串
'''


# list1 = [1,2,3]
# bool1 = True
# str1 = str(list1)
# print(str1)
# print(type(str1))
# print(type(str(bool1)))


'''
3、len(str)
功能：获取字符串的长度
字符串下标的取值范围[0,len(str)-1]
'''


# str1 = "hello"
# print(len(str1))
# list1 = [1,2,3,4]
# print(len(list1))
# print(str1[:10])


'''
4、str1.lower()
功能：将字符串中的大写字母转为小写字母，返回一个新的字符串
'''


# str1 = "HELLo, 11jerry!"
# print(str1.lower())


'''
5、str1.upper()
功能：将小写字母转为大写，返回一个新的字符串
'''


# print(str1.upper())
# print(str1)


'''
6、str1.swapcase()
功能：将大写字母转为小写字母，将小写字母转为大写字母，返回一个新的字符串
'''


# print(str1.swapcase())


'''
7、str1.capitalize()
功能：返回一个首字母大写，其他字母都小写的字符串
注意：若首字母不是字母则不处理
'''


# str2 = "123hello"
# print(str1.capitalize())
# print(str2.capitalize())


'''
8、str1.title()
返回一个所有单词首字母大写的字符串
'''


# str3 = "made in china"
# str4 = "made in USA"
# print(str3.title())
# print(str4.title())


'''
9、str1.center(width[,fillchar=' '])
参数一：指定长度【必须写】
参数二：填充字符【可不写，默认空格】
注意：fillchar只能是一个字符
返回一个以str1居中的长度为width的，两侧使用fillchar填充的新的字符串
str1.ljust(width[,fillchar])
str1.rjust(width[,fillchar])
注意：.center、.ljust、.rjust，这三个方法功能是类似的，只是文本的对其方式不同
str.center()：文本居中
str.ljust()：文本左对齐
str.rjust()：文本右对齐
'''


# print("开始游戏".center(50, "*"))
# print("开始游戏".ljust(50, "*"))
# print("开始游戏".rjust(50, "*"))


'''
10、str1.zfill(width)
此方法类似于str1.rjust()，只不过指定了使用0来进行填充
'''


# print("开始游戏".zfill(50))


'''
需求：从控制台输入一行字符串，要求字符串的长度必须大于等于20，
若长度不够则重新输入，输入完毕之后，统计一下数字的个数，并且将最后十个字符转为大写，前面十个为小写的。
打印转换之后的字符串还有数字的个数。

while True:
    input_str = input("请输入一行字符串（长度不小于20）：")
    if len(input_str) >= 20:
        break
    else:
        print("输入的长度%d有误"%len(input_str))
        
count = 0
for char in input_str:
    if "0" <= char <= "9":
        count += 1

left_ten = input_str[:10].lower()
right_ten = input_str[-10:].upper()
res_str = left_ten + input_str[10:-10] + right_ten

print("转换之后的字符串为：" + res_str)
print("数字出现的次数为：%d次"%count)
'''
