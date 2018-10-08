#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
w：若文件存在则覆盖，文件不存在则创建
a：若文件存在则追加，文件不存在则创建
'''

# with open('demo.txt', 'a') as f:
#     f.write('good')

'''
将 "FILENAME": "set.txt" 字符串添加到set.txt文件中，并且将set.txt读入到字典中。
'''

with open('set.txt', 'a+') as f:
    # 因为是以a+方式打开的，此时文件指针在文件末尾
    # 将文件指针移至开头
    # 文本文件每次只能指定一个相对文件开头的偏移量，否则会报错
    f.seek(0)
    fileContent = f.read()
    if not fileContent.endswith('\n'):
        f.write('\n')
    f.write('"FILENAME": "set.txt",\n')
    # 确保写入
    f.flush()
    f.seek(0)
    infoDict = {}
    while True:
        line = f.readline()
        if line == '':
            break
        lineList = line.split(': ')
        infoDict[lineList[0][1:-1]] = lineList[1][1:-3]
    print(infoDict)
