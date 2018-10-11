#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import re


'''
(xyz)   将小括号中的数据作为一个整体来匹配
x|y     表示匹配的x或者y
'''

'''
判断手机号码是否是合法的电信号码：
1、11位
2、数字
3、前三位：189，133,153,181,180,177
'''

phone1 = '12345678990'
phone2 = '18945678990'
phone3 = '13345678990'
phone4 = '15145678990'
print(re.match(r'^(189|133|153|181|180|177)\d{8}$', phone1))
print(re.match(r'^((189|133|153|181|180|177)\d{8})$', phone2))
print(re.match(r'^(189|133|153|181|180|177)\d{8}$', phone3))
print(re.match(r'^(189|133|153|181|180|177)\d{8}$', phone4))
