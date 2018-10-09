#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne

print()
'''
文件读写：
普通文件：
f = open(path, mode, encoding, error)
path:文件路径[文件路径必须存在]，可以是绝对路径也可以是相对路径
mode: r 读取文件
encoding:编码格式【一般情况下使用utf-8】
error：编码错误的处理【一般情况下使用ignore，忽略编码错误】
文件读取：
f.read() 一次性读取所有内容
f.read(size) 一次性读取size字节
配置文件一般使用下面的读取方式
f.readline() 一次性读取一行
f.readlines() 一次性读取所有行，并返回一个列表

# 关闭文件
f.close()

普通文件的写入：
f = open(path, mode, encoding, error)
path：文件路径【可以存在也可以是不存在的】
mode: w 写入文件【若path存在，则覆盖，若不存在则创建】
mode: a 写入文件【若path存在，则追加，若不存在则创建】
# 写入文件
f.write(str)
str：必须是字符串，可以是普通字符串，也可以是二进制字符串

# 关闭文件
# 确保文件全部写入磁盘
f.close()

建议使用
with open(path, mode, encoding, error) as f:
    f.read()
    # f.write()


二进制文件:
with open(path, mode) as f:
path：文件路径
mode：rb 读取文件
      wb 写入文件
      ab 写入文件【一般不用】
'''

'''
pickle模块
功能：此模块可以将对象序列化存入到文件中，
还可以将文件中的数据反序列化到内存中。

存储数据是以二进制的方式进行存储或者读取【mode:rb/wb】
pickle.dump(obj, f)
参数一：要序列化的对象
参数二：打开的文件
功能：将要序列化的对象存入到打开的文件中
res = pick.dumps(obj)
参数：将会指定的对象进行序列化，并且返回

pickle.load(f)
参数：打开的文件
功能：反序列化读取打开文件中所有内容

pickle.loads(byte)
参数：二进制字符串
功能：反序列化传入的二进制的字符串

注意：当有多个对象需要存入的时候，我们可以将多个对象存入序列中，写入或者读出。

json模块

json.dump(obj, f, default=func)
参数一：要写入的对象
参数二：打开的文件
参数三：将对象转为字典的函数【需要自己定制】
功能：将传入的对象使用指定的函数转为字典后，再序列化为字符串写入到打开的文件中

res = json.dumps(obj, default=func)
参数一：要写入的对象
参数二：将对象转为字典的函数【需要自己定制】
功能：将对象使用指定的函数转为字典并且序列化成字符串返回
f.write(res)

json.load(f, object_hook=func)
参数一：打开的文件
参数二：将字典转为对象的函数【需要手动定制】
功能：将打开文件的所有内容读出并且使用指定的函数，
将读出的内容反序列化成对象【返回一个对象】

json.load(str, object_hook=func)
参数一：要反序列化的字符串(字典形式)
参数二：将字典转为对象的函数【需要手动定制】
功能：将指定的字符串进行反序列化，并且转为指定的对象返回
'''
