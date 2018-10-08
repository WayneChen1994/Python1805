#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
在Python中使用的文件读写，是由Python给我们提供的一个内置函数。
一般情况下，系统不允许我们直接操作磁盘，所以对于磁盘操作，是由操作系统留下的接口，我们来进行调用。
因此我们的文件读写其实就是请求操作系统打开一个文件对象，然后通过操作系统的接口来读取或者写入文件。
'''

'''
open(path, encoding='utf-8', errors='ignore')
参数一：文件路径
参数二：指定文件的编码格式
参数三：若出现编码问题的错误则忽略不计
功能：请求打开一个文件对象

f.read()
功能：读取文件

f.close()
功能：关闭文件
注意：打开的文件必须关闭，
1、因为打开的文件会占用内存
2、系统同一时间能够打开的文件对象也是有限制的
因此，使用完毕之后，我们必须要文件对象关闭
'''

'''
try:
    # 有可能发生异常的语句
    语句块
except:
    # 捕捉到异常的时候执行的语句
    语句块
finally:
    # 无论是否发生异常都会执行此语句
    语句块
'''

# f = open('test.txt', encoding='utf-8', errors='ignore')
# print(f.read())
# f.close()


# try:
#     f = None
#     f = open('test1.txt')
#     print(f.read())
# finally:
#     # 判空处理
#     if f:
#         print('关闭文件')
#         f.close()
#     else:
#         print('文件为空')


'''
简写后的语句
with open(path, encoding) as 文件描述符:
    文件描述符.read()

注意：使用此语句我们不必手动关闭文件对象，当我们此语句下的语句块执行结束之后，文件会自动关闭。
'''


with open('test.txt', encoding='utf-8') as f:
    print(f.read())
