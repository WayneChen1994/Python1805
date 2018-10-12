#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


import pygame
import time


# 初始化音频
pygame.mixer.init()


# 加载音乐
pygame.mixer.music.load("dang.mp3")


# 播放音乐
pygame.mixer.music.play()
time.sleep(30)


'''
音乐播放器
1、上一曲
2、下一曲
3、暂停
4、播放
5、音量大小
6、退出
使用函数完成

首先进入欢迎页面：
******************
* 欢迎来到酷我播放器 *
*                *
******************
进入功能区
**********************
* 1、上一曲 2、下一曲    *
* 3、暂停  4、播放       *
* 5、音量调大 6、音量调小  *
*  7、退出              *
***********************
'''
