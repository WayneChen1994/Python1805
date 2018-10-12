#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock.connect(('10.3.134.23', 9090))

while True:
    recvStr = sock.recv(1024).decode()
    print("服务器说：", recvStr)
    inputStr = input("请输入发送的消息：")
    sock.send(inputStr.encode())
    if inputStr == 'bye':
        break


sock.close()
