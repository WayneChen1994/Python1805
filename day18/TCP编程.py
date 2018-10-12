#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
socket是一个网络编程的抽象概念，我们通常用它来表示打开一个网络连接，
打开一个网络连接的时候，我们需要知道对方IP地址以及端口号
再指定网络协议即可。
'''


'''
大多数创建可靠连接的是使用TCP协议
客户端：主动创建连接的是客户端
服务器：被动响应的是服务器
'''


import socket
import re


'''
参数一：指定IP协议，socket.AF_INET IPV4协议；
socket.AF_INET6 IPV6协议
参数二：指定的TCP协议
'''
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


'''
客户端主动创建链接的时候，需要知道对方的IP地址以及端口号，
但是一般情况下，一些服务器会给出一个域名而不是IP地址，
我们通过域名可以间接地转接到其IP地址，端口号如何确定呢？
网页的端口号固定80，因此请求网络的服务器的时候，端口号直接使用80即可
STMP【邮件】25

注意：地址是一个元组，但是地址中包含ip地址与端口号
'''
sock.connect(('www.zxxk.com', 443))


'''
发送请求
'''
sock.send(b'GET / HTTP/1.1\r\nHost:www.zxxk.com\r\nConnection:close\r\n\r\n')
dataAll = b''
while True:
    data = sock.recv(1024*1024)
    dataAll += data
    if data == b'':
        break

html = dataAll.decode('gbk')
print(html)
sock.close()


'''
把请求回来的数据拆分成两个部分，文件头的部分存储在head.txt文件中，文件体的部分存在index.html文件中
'''


alist = re.split(r'\r\n\r\n', html, maxsplit=1)


with open('head.txt', 'w', newline='') as f:
    f.write(alist[0])

with open('index.html', 'w', newline='') as f2:
    f2.write(alist[1])
