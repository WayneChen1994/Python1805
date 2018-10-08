#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
当文件中出现视频、音频或者图片的时候，我们的文件读写需要使用二进制的方式来进行读写。
open(path, "rb") 读取文件
'''

# with open('ddl.jpg', 'rb') as f:
#     print(f.read())

str1 = '中国'.encode()
print(str1)

with open('ddl.jpg', 'rb') as f:
    str2 = f.read()
    print(str2)
    print(type(str2))
