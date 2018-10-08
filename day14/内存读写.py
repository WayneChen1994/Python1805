#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
在内存读取字符串
'''

from io import StringIO


f = StringIO()
f.write('hello')
f.write('world')
print(f.getvalue())


str1 = 'hello'
str2 = 'world'
print(str1+str2)


f2 = StringIO("hello world")
print(f2.read())


str3 = 'hello world'
print(str3)

print("*"*50)
'''
在内存中读取二进制数据
'''


from io import BytesIO

f3 = BytesIO()
f3.write("中国".encode())
f3.write("aaaaabbdvc".encode())
f3.write(b"aaaaabbdvc")
print(f3.getvalue())

f4 = BytesIO(b'\xe4\xb8\xad\xe5\x9b\xbd')
# print(f4.read().decode())
print(f4.getvalue().decode())
