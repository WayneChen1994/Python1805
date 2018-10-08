#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
序列化：
将内存中的变量变成可存储的过程我们称之为序列化【序列化对象】

反序列化：
将磁盘中的数据重新读入到内存的过程，我们称之为反序列化
'''

'''
import pickle

dict1 = {'name': 'lili', 'age': 18}

with open('user.txt', 'wb') as f:
    # 要写入的对象
    # 打开的文件对象
    pickle.dump(dict1, f)

with open('user.txt', 'rb') as f2:
    # 读取文件
    res = pickle.load(f2)
    print(res)
    print(type(res))
'''

'''
需求：将一个字典存入到一个文件中，并且读出【字典】
'''

# adict = {'name': 'wayne', 'age':'23', 'hobby': 'money'}
#
# with open('user2.txt', 'w') as f:
#     f.write(str(adict))
#
# with open('user2.txt', 'r') as f2:
#     res = f2.read()
#     print('res =', res)
#     print('res类型为：', type(res))
#     adict = {}
#     alist = res[1:-1].split(', ')
#     for x in alist:
#         blist = x.split(': ')
#         adict[blist[0][1:-1]] = blist[1][1:-1]
#     print('adict =', adict)
#     print('adict类型为：', type(adict))

dict1 = {'name': 'lili', 'age': 18}
with open('dict1.txt', 'w') as f3:
    f3.write(str(dict1))

with open('dict1.txt', 'r') as f4:
    res2 = f4.read()
    print(res2)
    print(type(res2))
    res3 = eval(res2)
    print(type(res3))
