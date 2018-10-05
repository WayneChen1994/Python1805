'''
可迭代对象：
能作用于for循环的，我们统称为可迭代对象
本质是复写了__iter__

1、常见的可迭代对象：
list/tuple/set/dict/range/str
2、生成器：可以一边循环一边推算出下一个元素
像这样的机制我们称为生成器【优点：节约内存】
'''

'''
如何创建生成器？
将列表生成式的[]改为()，则就为生成器
'''
from collections import Iterable


list1 = [x for x in range(1, 101)]
g = (x for x in range(1, 101))
print(type(list1))
print(type(g))
print(next(g))

print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance(range(10), Iterable))
print(isinstance("", Iterable))
print(isinstance({}, Iterable))
print(isinstance({12, 34}, Iterable))
