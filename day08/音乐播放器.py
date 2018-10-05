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
import time
import pygame

# 初始化音频部分
pygame.mixer.init()

def welcome():
    print('''
        ******************
        * 欢迎来到酷我播放器 *
        *                *
        ******************
        ''')


def select():
    print('''
        **********************
        * 1、上一曲 2、下一曲   *
        * 3、停止  4、播放      *
        * 5、音量调大 6、音量调小 *
        *  7、退出             *
        ***********************
        ''')
    num = input("请输入您要操作的序号：")
    return num


def playMusic(path, volume=0.5):
    # 加载音乐
    pygame.mixer.music.load(path)
    # 设置默认音量
    pygame.mixer.music.set_volume(volume)
    # 播放音乐
    pygame.mixer.music.play()


def shang(index, musicList, volume):
    if index <= 0:
        print("已经是第一首音乐了")
    else:
        index -= 1
        playMusic(musicList[index], volume)
    return index


def xia(index, musicList, volume):
    if index >= len(musicList) - 1:
        print("当前音乐已经是最后一首了")
    else:
        index += 1
        playMusic(musicList[index], volume)
    return index


def upVol():
    current_vol = pygame.mixer.music.get_volume()
    now_vol = current_vol + 0.1
    if now_vol >= 1:
        print("已经是最大音量了")
        now_vol -= 0.1
    else:
        print("音量调大")
        pygame.mixer.music.set_volume(now_vol)
    return now_vol


def DownVol():
    current_vol = pygame.mixer.music.get_volume()
    now_vol = current_vol - 0.1
    if now_vol <= 0:
        print("已经是最小音量了")
        now_vol += 0.1
    else:
        print("音量调小")
        pygame.mixer.music.set_volume(now_vol)
    return now_vol


welcome()
musicList = ["dang1.mp3", "dang2.mp3", "dang3.mp3",
             "dang4.mp3", "dang5.mp3"]
index = 0
volume = 0.5
while True:
    time.sleep(2)
    num = select()
    if num == "1":
        if pygame.mixer.get_busy() == 1:
            print("上一曲")
            index = shang(index, musicList, volume)
        else:
            print("当前未播放歌曲！")
    elif num == "2":
        if pygame.mixer.get_busy() == 1:
            print("下一曲")
            index = xia(index, musicList, volume)
        else:
            print("当前未播放歌曲！")
    elif num == "3":
        print("停止")
        pygame.mixer.music.stop()
    elif num == "4":
        print("播放")
        playMusic(musicList[index], volume)
    elif num == "5":
        volume = upVol()
    elif num == "6":
        volume = DownVol()
    elif num == "7":
        print("退出")
        break
    print("*" * 50)
    if pygame.mixer.music.get_busy() == 1:
        print("当前音量:", pygame.mixer.music.get_volume())
        print("当前播放曲目：", musicList[index])
    else:
        print("请先播放音乐～")
    print("*" * 50)
