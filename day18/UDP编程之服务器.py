#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
UDP与TCP的区别：UDP面向的是无连接协议，使用UDP协议时，
我们不需要创建连接，但是需要知道对方的IP地址以及端口号。
优点：速度快
缺点：不可靠
应用：对于一些不要求可靠到达的数据，我们使用UDP，通常，语音视频通话
'''


import socket


# 参数一：IP协议
# 参数二：UDP协议
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# 绑定地址，地址包含ip地址以及端口号
sock.bind(('127.0.0.1', 9999))


while True:
    # 接收数据
    data, addr = sock.recvfrom(1024)
    print(data, addr)
    # 发送数据
    sock.sendto(b'server'+data, addr)
    sock.close()
    break
