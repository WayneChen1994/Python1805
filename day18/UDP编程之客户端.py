#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# 参数一：要发送的数据
# 参数二：发送的地址
sock.sendto(b'hello', ('127.0.0.1', 9999))


print(sock.recv(1024))
