#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


# 发送邮件的库
import smtplib
# 邮件文本的类
from email.mime.text import MIMEText


# 发送人的邮箱地址，以及授权码
sender = 'waynechen1994@163.com'
password = '39miku0831'


# 将字符串转为邮件文本
msg = MIMEText('试试用Python发送邮件^_^')


# 标题
msg['Subject'] = '用Python发送邮件'
# 发送者
msg['From'] = sender
# 收件人
msg['To'] = sender


# 请求SMTP服务器，端口号一般为25，服务器为smtp.163.com
mailServer = smtplib.SMTP('smtp.163.com', 25)
# 登陆
mailServer.login(sender, password)
# 发送邮件
# 参数一：发送人的地址
# 参数二：发送给谁，是一个列表，可以群发
# 参数三：发送的内容
mailServer.sendmail(sender, sender, msg.as_string())
# 退出邮箱
mailServer.quit()
