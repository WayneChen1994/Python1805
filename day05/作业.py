#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


print()


'''
1.从控制台输入一个正数n，则打印n行*
    *
  * *
* * *

n = int(input("请输入一个正整数："))
for x in range(1, n+1):
    space = n - x
    star = x
    print(" "*space + "*"*star)

'''


'''
2.冒泡排序，从控制台输入一个数值列表，对列表进行冒泡排序

input_str = input("请输入多个数值，中间用空格分隔：")
# 对输入的字符串进行切片操作，得到一个元素为字符串类型数字的列表
alist = input_str.split()
# 定义一个新列表，将原列表中每一个字符串类型的数字转成数字在添加到该新列表newList中，这样才能进行数字的排序操作
newList = []


for i in alist:
    newList.append(int(i))


# 获取数字的个数
length = len(newList)


# 对newList进行排序操作
# 外层循环用来确定冒泡排序需要几轮循环
for x in range(length-1):
    # 内层循环用来确定每一次循环需要比较的范围
    for y in range(length-1-x):
        # 冒泡排序（降序）
        # 如果前一个元素小于后一个元素
        if newList[y] < newList[y+1]:
            # 交换元素的位置
            newList[y], newList[y+1] = newList[y+1], newList[y]


print("冒泡排序的结果：", newList)

'''


'''
3.输入一个时间，获取这个时间的下一秒

import time


while True:
    timeStr = input("请输入一个时间（时:分:秒）：")
    #对该时间字符串进行切片操作，得到一个列表，元素为时分秒对应的数字
    timeList = timeStr.split(":")
    #得到时分秒对应的数字
    h = int(timeList[0])
    m = int(timeList[1])
    s = int(timeList[2])
    #进行数字的有效性验证
    if 0<=h<24 and 0<=m<60 and 0<=s<60:
        break
    else:
        print("输入的时间非法，请重新输入！")


while True:
    #得到下一秒
    s += 1
    #当秒或分为60、以及时为24的情况需要处理
    if s == 60:
        m += 1
        s = 0
        if m == 60:
            h += 1
            m = 0
            if h == 24:
                h = 0
    time.sleep(1)
    #不停地打印下一秒，只想打印一次则去掉While True
    print("下一秒为：%02d:%02d:%02d" % (h, m, s))

'''


'''
4.歌词解析器
1.把歌词进行解析切片处理，把时间转成对应的浮点数
2.使用字典将时间与歌词进行存储{时间：歌词}
3.循环自动打印歌词【结束循环的条件，key为None的时候】
'''


musicLrc = '''[00:03.50]传奇
[00:19.10]作词：刘兵 作曲：李健
[00:20.60]演唱：王菲
[00:26.60]    
[04:40.75][02:39.90][00:36.25]只是因为在人群中多看了你一眼
[04:49.00]
[02:47.44][00:43.69]再也没能忘掉你容颜
[02:54.83][00:51.24]梦想着偶然能有一天再相见
[03:02.32][00:58.75]从此我开始孤单思念
[03:08.15][01:04.30]
[03:09.35][01:05.50]想你时你在天边
[03:16.90][01:13.13]想你时你在眼前
[03:24.42][01:20.92]想你时你在脑海
[03:31.85][01:28.44]想你时你在心田
[03:38.67][01:35.05]
[04:09.96][03:39.87][01:36.25]宁愿相信我们前世有约
[04:16.37][03:46.38][01:42.47]今生的爱情故事 不会再改变
[04:24.82][03:54.83][01:51.18]宁愿用这一生等你发现
[04:31.38][04:01.40][01:57.43]我一直在你身旁 从未走远
[04:39.55][04:09.00][02:07.85]
'''


# 将多行文本按行切割，得到一个初始列表，保存每一行的字符串
baseList = musicLrc.splitlines()
# 定义一个字典，用于保存时间和歌词的对应信息：{时间:歌词}
resDict = {}


# 遍历每一行，对每一行进行二次切片操作，提取出歌词串、时间列表
for line in baseList:
    lyTime = 0
    tempList = line.split("]")
    # 取出歌词文本
    lyStr = tempList.pop()
    # 剩下的其实就是时间列表
    for i in tempList:
        timeStr = i.split("[")[-1]
        # 对该时间字符串进行切片，提取出分与秒并将时间计算成一个浮点数（秒）
        timeList = timeStr.split(":")
        # 计算得出以浮点数表示的时间（秒）
        lyTime = float(timeList[0]) * 60 + float(timeList[1])
        # 将时间作为Key、歌词文本作为Value，保存进字典
        resDict[lyTime] = lyStr


# 将所有的时间点保存进一个列表，对列表进行升序排列
# 依次遍历该列表，将其元素作为Key依次去resDict中取出歌词
sortList = []


for atime in resDict:
    sortList.append(atime)
sortList.sort()


import time


# 控制停顿时间
sleepTime = sortList[0]


for index, t in enumerate(sortList):
    # 当前时间点
    currentTime = t
    # 进行判断防止下标越界
    if index <= len(sortList) - 2:
        # 下一个时间点
        nextTime = sortList[index + 1]
        # 停顿
        time.sleep(sleepTime)
        # 播放下一句歌词之前应该停顿的时间
        sleepTime = nextTime - currentTime
        # 打印歌词
        if resDict.get(t) == None:
            break
        else:
            print(resDict.get(t))
