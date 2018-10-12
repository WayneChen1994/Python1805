#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
双冒号的使用
list1[start:end:step]
start：默认为0
end：默认为取到最后
step：步长，默认为1
注意：当step为-1的时候，可以进行列表的反转
'''


# list1 = [1, 2, 3, 4, 6, 5]
# print(list1[1:])
# print(list1[:-1])
# print(list1[::2])
# print(list(range(100))[::-2])
# print(list(range(100))[::])


# list2 = ["hello", "good", "nice", "yes", "ok"]
# list3 = [1, 2, 3, 4, 5]
# list4 = ["1", "2", "3", "4", "5"]
# res = zip(list2, list3)
# print(list(res))
# list6, list7 = list(zip(*res))
# print(list6)
# print(list7)


'''
需求：
list2 = ["hello","good","nice","yes","ok"]
list3 = [1, 2, 3, 4, 5]
将这两个列表转为字典
'''


list2 = ["hello", "good", "nice", "yes", "ok"]
list3 = [1, 2, 3, 4, 5]
print(dict(zip(list3, list2)))


'''
zip(iter)
功能：使用zip函数它能将传进去的可迭代对象一一对应打包成一个一个的元组，然后将元组存放在一个迭代器中，并且返回
【Python2.x返回列表】
当传入的可迭代对象的长度不一致的时候，返回的迭代器器的长度与长度最短的可迭代对象保持一致
当使用*的时候，我们可以将已经打包好的可迭代对象，解包为打包前的一个状态。
'''
