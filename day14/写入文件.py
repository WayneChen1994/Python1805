#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
读取文件与写入文件使用的函数都是相同的，唯一不同的是
读取文件的时候使用"r"或者是"rb"，
写入文件的时候使用"w"或者"wb"

若文件存在，则覆盖之前的内容，若文件不存在则新建一个文件。
'''

# with open('demo1.txt', 'w') as f:
#     f.write("hello")

'''
需求：将set.txt文件读取出，并且写入到set2.txt中
'''

# with open('set2.txt', 'w') as f1:
#     with open('set.txt', 'r') as f2:
#         f1.write(f2.read())


# with open('set.txt', 'r') as f:
#     with open('set2.txt', 'w') as f2:
#         while True:
#             res = f.readline()
#             if res == '':
#                 break
#             else:
#                 f2.write(res)


'''
需求：将img.jpg读出，并且写入到img2.jpg中
'''

with open('img.png', 'rb') as f:
    with open('img2.png', 'wb') as f2:
        while True:
            content = f.readline()
            if content == b'':
                break
            f2.write(content)
