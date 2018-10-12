#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import socket
import random


'''
参数一：指定IP协议
参数二：指定TCP协议
'''


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind(address) address是一个元组，绑定IP地址以及端口号
# ip地址：本机IP
# 端口号：1024之后，可以自己设定
sock.bind(('10.3.134.23', 9090))
# 监听端口，传入的参数是指最大连接客户端数量
sock.listen(6)


sayList = ["今天天气不错", "心情不好", "我中奖了", "哦是吗", "你以为呢", "哈哈好吧", "你说的都对", "那有怎么样", "你很了不起啊"]


'''
需求：若存在多条数据收发的时候如何解决？
'''


# 服务器处于一个常开的状态
while True:
    s, addr = sock.accept()
    s.send('客官好啊～'.encode())
    while True:
        s.send(random.choice(sayList).encode())
        content = s.recv(1024).decode()
        if content == 'bye':
            s.send('再见了兄弟'.encode())
            break
        print("客户端说：", content)
