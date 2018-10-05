'''
set集合的概述：
本质：是一个无序的并且不重复的集合
'''

'''
set集合的创建：
集合名 = set([1,2,3])
集合名 = {元素1，元素2，……，元素n}
创建一个空的set集合
set1 = set()
'''
set1 = {12}
set2 = set()
print(type(set1))
print(type(set2))
print(set2)
list1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 0, 0]
set3 = set(list1)
print(list(set3))
