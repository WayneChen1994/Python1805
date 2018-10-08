#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
当文件过大的时候，我们通常情况下，不会一次性将所有文件读取到内存中。
'''

with open('test.txt', encoding='utf-8') as f:
    # 循环读取
    # print(f.read(100))
    while True:
        file1 = f.read(100)
        print(file1)
        if file1 == "":
            break
    print("读取完毕")
    print(f.read())
