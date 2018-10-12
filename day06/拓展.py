#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
音乐播放器
1.上一曲，
2.下一曲
3.暂停
4.播放
5.音量大小
6.退出
使用函数完成

首先进入欢迎页面：
***********************
*   欢迎来到酷我播放器 *
*                     *
***********************
进入功能区
***********************
* 1.上一曲     2.下一曲*
* 3.暂停       4.播放  *
* 5.音量调大  6.音量调小*
*     7.退出           *
************************
'''


import pygame
import time


musicStr = '''[00:01.49]动力火车 - 当
[00:20.53]当 《还珠格格》主题曲（动力火车）
[00:21.89]喔...喔..喔.喔.喔
[00:28.60]喔...喔..喔.喔.喔
[00:35.44]喔...喔..喔.喔.喔
[00:42.27]喔...喔..喔
[00:52.01]当山峰没有棱角的时候
[00:55.39]当河水不再流
[00:58.79]当时间停住 日夜不分
[01:02.67]当天地万物化为虚有
[01:05.58]我还是不能和你分手
[01:09.70]不能和你分手
[01:12.47]你的温柔是我今生最大的守候
[01:19.19]当太阳不再上升的时候
[01:22.69]当地球不再转动
[01:26.12]当春夏秋冬 不再变化
[01:29.89]当花草树木全部凋残
[01:32.81]我还是不能和你分散
[01:37.10]不能和你分散
[01:39.67]你的笑容是我今生最大的眷恋
[01:42.00]歌词制作:CzBoy QQ:41304064
[01:46.79]让我们红尘作伴 活的潇潇洒洒
[01:50.72]策马奔腾 共享人世繁华
[01:54.17]对酒当歌唱出心中喜悦
[01:57.59]轰轰烈烈把握青春年华
[02:00.72]让我们红尘作伴 活的潇潇洒洒
[02:04.32]策马奔腾 共享人世繁华
[02:07.89]对酒当歌唱出心中喜悦
[02:11.37]轰轰烈烈把握青春年华
[02:18.26]喔...喔..喔.喔.喔
[02:25.17]喔...喔..喔.喔.喔
[02:38.78]喔...喔..喔.喔.喔
[02:38.69]喔...喔..喔
[02:48.80]当太阳不再上升的时候
[02:51.95]当地球不再转动
[02:55.42]当春夏秋冬 不再变化
[02:59.25]当花草树木全部凋残
[03:02.29]我还是不能和你分散
[03:06.13]不能和你分散
[03:09.11]你的笑容是我今生最大的眷恋
[03:16.25]让我们红尘作伴 活的潇潇洒洒
[03:19.91]策马奔腾 共享人世繁华
[03:23.35]对酒当歌唱出心中喜悦
[03:26.80]轰轰烈烈把握青春年华
[03:29.74]让我们红尘作伴 活的潇潇洒洒
[03:33.52]策马奔腾 共享人世繁华
[03:36.98]对酒当歌唱出心中喜悦
[03:40.46]轰轰烈烈把握青春年华
[03:46.71]让我们红尘作伴 活的潇潇洒洒
[03:50.62]策马奔腾 共享人世繁华
[03:54.07]对酒当歌唱出心中喜悦
[03:57.46]轰轰烈烈把握青春年华
[04:00.29]让我们红尘作伴 活的潇潇洒洒
[04:04.30]策马奔腾 共享人世繁华
[04:07.76]对酒当歌唱出心中喜悦
[04:11.16]轰轰烈烈把握青春年华'''


def getMusicDict(mStr):
    mStrList = mStr.splitlines()
    resDict = {}
    for line in mStrList:
        alist = line.split("]")
        lyStr = alist.pop()
        timeStr = alist[0][1:]
        blist = timeStr.split(":")
        timeFloat = float(blist[0]) * 60 + float(blist[1])
        resDict[timeFloat] = lyStr
    return resDict


def startPlayer():
    print("*" * 50)
    print("*", end="")
    print("欢迎来到酷我播放器".center(42, " "), end="")
    print("*")
    print("*" * 50)


def showOptions():
    print("进入功能区".center(45, " "))
    print("*" * 50)
    print("*", end="")
    print("1、上一曲 2、下一曲".center(42, " "), end="")
    print("*")
    print("*", end="")
    print("3、暂停 4、播放".center(44, " "), end="")
    print("*")
    print("*", end="")
    print("5、音量调大 6、音量调小".center(41, " "), end="")
    print("*")
    print("*", end="")
    print("7、退出".center(46, " "), end="")
    print("*")
    print("*" * 50)


def playControl(option, songList):
    pygame.mixer.init()
    pygame.mixer.music.load(songList[songIndex])
    soundValue = 0.5
    songIndex = 1
    pygame.mixer.music.set_volume(soundValue)
    if option == "1":
        if songIndex - 1 >= 0:
            print("正在切换到上一曲……")
            time.sleep(1)
            pygame.mixer.music.load(songList[songIndex - 1])
            pygame.mixer.music.play()
            lyricPlay(getMusicDict(musicStr))
        else:
            print("已经是第一首歌曲，无法切换！")
    elif option == "2":
        if songIndex + 1 <= len(songList) - 1:
            print("正在切换到下一曲……")
            time.sleep(1)
            pygame.mixer.music.load(songList[songIndex + 1])
            pygame.mixer.music.play()
            lyricPlay(getMusicDict(musicStr))
            print("已经是最后一首歌曲，无法切换！")
    elif option == "3":
        if pygame.mixer.music.get_busy() == 1:
            print("音乐暂停～")
            pygame.mixer.music.pause()
            # 不知道如何让歌词也同步暂停？
        else:
            print("当前未处于播放状态～")
    elif option == "5":
        soundValue += 0.1
        if soundValue <= 1:
            pygame.mixer.music.set_volume(soundValue)
            print("音量调大～")
        else:
            print("已经是最大音量")
    elif option == "6":
        soundValue -= 0.1
        if soundValue >= 0:
            pygame.mixer.music.set_volume(soundValue)
            print("音量调小～")
        else:
            print("已经是最小音量")
    elif option == "7":
        if pygame.mixer.music.get_busy() == 1:
            print("结束播放……")
            time.sleep(1)
            pygame.mixer.music.stop()
        else:
            print("当前未处于播放状态～")


def lyricPlay(musicDict):
    keyList = [x for x in musicDict]
    time.sleep(keyList[0])
    for index in range(len(keyList)):
        print(musicDict.get(keyList[index]))
        if index > 0:
            time.sleep(keyList[index] - keyList[index - 1])


startPlayer()


while True:
    showOptions()
    option = input("请选择一项操作：")
    songList = ["dang.mp3", "dang.mp3", "dang.mp3",
                "dang.mp3", "dang.mp3", "dang.mp3", "dang.mp3"]
    playControl(option, songList)
