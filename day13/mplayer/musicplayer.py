#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
音乐播放器
特征：歌曲【通过OS模块加载歌曲】 正在播放的 声音
行为：播放，暂停，上一曲，下一曲，声音调大，声音调小，退出
'''
import os, time, pygame

class MusicPlayer:
    musicList = []
    current = 0
    volume = 0.5

    @staticmethod
    def welcome():
        print('''
            **********************
            *                    *
            *   Wayne的音乐播放器   *
            *                    *
            **********************''')


    @staticmethod
    def select():
        print('''
            **********************
            *  1.播放   2.暂停     *
            * 3.上一曲 4.下一曲     *
            * 5.音量调大 6.音量调小  *
            *       0.退出        *
            **********************''')
        num = input("请输入您要操作的选项：")
        return num


    # 加载音乐列表
    @classmethod
    def loadMusicList(cls, path):
        filesList = os.listdir(path)
        for filename in filesList:
            absFilePath = os.path.join(path, filename)
            if os.path.isfile(absFilePath) and filename[-3:] == "mp3":
                cls.musicList.append(absFilePath)
            elif os.path.isdir(absFilePath):
                cls.loadMusicList(absFilePath)
        pygame.mixer.init()
        return cls.musicList


    # 播放当前音乐
    @classmethod
    def playMusic(cls, current):
        currentMusic = cls.musicList[current]
        pygame.mixer.music.load(currentMusic)
        pygame.mixer.music.play()


    # 暂停当前音乐
    @staticmethod
    def pauseMusic():
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        else:
            print("当前尚未播放音乐")

    # 播放上一曲
    @classmethod
    def playPrev(cls, index):
        if index > 0:
            cls.current -= 1
            if pygame.mixer.music.get_busy():
                pygame.mixer.stop()
            cls.playMusic(cls.current)
        else:
            print("已经是第一首曲子了")


    # 播放下一曲
    @classmethod
    def playNext(cls, index):
        if index < len(cls.musicList) - 1:
            cls.current += 1
            if pygame.mixer.music.get_busy():
                pygame.mixer.stop()
            cls.playMusic(cls.current)
        else:
            print("已经是最后一首曲子了")


    # 音量调大
    @classmethod
    def volUp(cls):
        if cls.volume+0.1 <= 1:
            cls.volume += 0.1
            print("音量调大")
            pygame.mixer.music.set_volume(cls.volume)
        else:
            print("已经是最大音量了")


    # 音量调小
    @classmethod
    def volDown(cls):
        if cls.volume-0.1 >= 0.1:
            cls.volume -= 0.1
            print("音量调小")
            pygame.mixer.music.set_volume(cls.volume)
        else:
            print("已经是最小音量了")


if __name__ == "__main__":
    MusicPlayer.welcome()
    path = input("准备扫描音乐，请输入一个文件路径：")
    MusicPlayer.musicList = MusicPlayer.loadMusicList(path)
    print("音乐播放列表：", MusicPlayer.musicList)
    while True:
        if pygame.mixer.music.get_busy():
            print("="*80)
            print("播放列表一共有%d首曲子，当前是第%d首" % (len(MusicPlayer.musicList), MusicPlayer.current+1))
            print("当前播放音乐：", os.path.basename(MusicPlayer.musicList[MusicPlayer.current]))
            print("当前音量：%.1f"%MusicPlayer.volume)
            print("=" * 80)
        choice = MusicPlayer.select()
        if choice == "1":
            print("播放")
            MusicPlayer.playMusic(MusicPlayer.current)
        elif choice == "2":
            print("暂停")
            MusicPlayer.pauseMusic()
        elif choice == "3":
            print("上一曲")
            MusicPlayer.playPrev(MusicPlayer.current)
        elif choice == "4":
            print("下一曲")
            MusicPlayer.playNext(MusicPlayer.current)
        elif choice == "5":
            print("声音调大")
            MusicPlayer.volUp()
        elif choice == "6":
            print("声音调小")
            MusicPlayer.volDown()
        elif choice == "0":
            print("退出")
            break
        else:
            print("无效的操作，请重新输入")
