#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


from functools import reduce


list1 = [1, 2, 3, 4, 23, 12, 34, 45]
list1.sort()
# print(list1)


'''
需求：按照字符串的字面量来进行排序
list2 = ["1", "2", "3", "4", "23", "12", "34", "45"]
'''

list2 = ["1", "2", "3", "4", "23", "12", "34", "45"]

list3 = list(map(int, list2))
list3.sort()
# print(list(map(str, list3)))


'''
sorted(iter, key, reverse)
参数一：参与比较的可迭代对象/序列
有且只有一个参数
参数二：key后面跟的是比较的函数
参数三：reverse默认情况下为False【升序】
       reverse=True【降序】
功能：序列中的每一个元素先作用于key后面的函数，然后比较key后面函数得到的值
注意：返回的结果是一个序列
'''


list4 = sorted(list2, key=int, reverse=True)
# print(list4)


list5 = [1, 2, 3, -1, -3, -3.4, 89, -345, -0.9]


'''
需求：对list5进行排序，按照绝对值大小排，降序
'''


list6 = sorted(list5, key=abs, reverse=True)
# print(list6)


'''
需求：按照年龄升序排序
data = [["jerry", 28, "老鼠"], ["tom", 25, "无"], ["hanmeimei", 26, "金钱"]]
'''


data = [["jerry", 28, "老鼠"], ["tom", 25, "无"], ["hanmeimei", 26, "金钱"]]


list7 = sorted(data, key=lambda x:x[1])
# print(list7)


'''
需求：按照列表中字符串的长度进行排序
'''
list8 = ["123", "asdsfd", "edrft", "", "sfdg", "ewhf9r3vtr", "dcbbbbbbbb"]
# print(sorted(list8, key=len, reverse=True))


'''
求列表中元素字面量为偶数的和
'''


list9 = [1, "2", "23", "45", 89, "98", "75", 34, 46, 77, 90]


print(reduce(lambda a,b:a+b, filter(lambda x:x%2==0, map(int, list9))))
