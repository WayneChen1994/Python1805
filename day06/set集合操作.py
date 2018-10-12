#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
set集合元素的添加
set1.add(element)
1、注意：添加的元素重复的时候，不会报错但没有效果
2、添加的元素必须是不可变的，比如不能是list/dict/set
'''


set1 = set()
set1.add(12)
set1.add(22)
set1.add(32)
set1.add(12)
print(set1)
# set1.add({12, 34, 34, 45})


'''
set1.update(iterable)
功能：将可迭代对象打碎插入到set集合中
注意：参数必须是可迭代对象
'''


set1.update("hello")
set1.update(["hello", "good", "nice"])
set1.update(("hello1", "good1"))
print(set1)


'''
set1.remove(元素)
功能：移除指定的元素

len(set)
功能：获取set集合的长度
'''


set1.remove("good")
print(set1)


for x in set1:
    print(x)


for index, data in enumerate(set1):
    print(index, data)


print(len(set1))


set2 = {12, 34, 56, 78, "hello", "nice"}
print(set1)
print(set2)


'''
set1&set2
求两个集合的交集【相同的部分】
set1|set2
求两个集合的并集【两个相加后去除重复的部分】
'''


print(set1 & set2)
print(set1 | set2)
