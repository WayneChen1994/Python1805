#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import csv



with open("demo.csv", "a", encoding="utf-8", newline="") as f:
    # 获取一个csvwriter对象
    csvwriter = csv.writer(f)
    # 一行，一行写入文件，注意写入的数据为列表
    csvwriter.writerow([1, 2, 3])
    csvwriter.writerow([4, 5, 6])


'''
将csv读出的数据，写入到一个新的文件中去【new.csv】
写成一个函数。
'''


def getList(path, num, col):
    infolist = []
    with open(path, "r", errors="ignore") as f:
        csvReader = csv.reader(f)
        for x in range(num):
            info = next(csvReader)
            infolist.append(info[:col])
    return infolist


# 传入的列表是一个二维列表
def writeCsvFile(path, data):
    # path：打开文件的路径
    # w：写入文件
    # encoding：指定编码格式
    # newline=""：去除写入的时候自带的换行
    with open(path, "w", encoding="utf-8", newline="") as f:
        csvw = csv.writer(f)
        # 遍历二维列表
        for line in data:
            # 将子列表取出，并且写入到文件
            csvw.writerow(line)


list1 = getList("democsv.csv", 30, 5)
writeCsvFile("new.csv", list1)
