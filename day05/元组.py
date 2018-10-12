#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author: Wayne.Chen


'''
元组的定义：
本质上来讲也是一种有序的集合，与列表非常相似，
表现形式有所不同，列表使用[]，而元组使用()
特点：一旦初始化，则不能修改
注意：初始化就不能修改，指的是初始化之后，元组对于它内部元素的指向是不发生变化的
'''


'''
元组的创建：
元组名 = (元素1，元素2，……，元素n)
注意：当元组中只有一个元素的时候，我们需要在此元素的后面加一个逗号来进行消除歧义（此括号为元组）
'''


tuple1 = ()
tuple2 = (1)
tuple3 = (1, 3, 4)
tuple4 = tuple()
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))
print(type(tuple4))


'''
元组元素的访问
语法：
元组名[下标]
下标/索引值可以为正【从左往右】
也可以为负【从右往左】
注意：不要下标越界
'''


tuple1 = (12, 34, 45, 56, "hello")
tuple2 = (12, (12, 34, 45, 56, "hello"), 34, 45, 56)
tuple3 = (12, [12, 34, 45, 56, "hello"], 34, 45, 56)


print(tuple1[-1])
print(tuple2[1][-1])
# print(tuple3[1][-1])
print(tuple3[1])


'''
修改元组：
元组中的元素,一旦初始化则不能修改，但是，元组中是可以放列表的，而列表是可以修改的，
我们可以通过修改列表中的元素来间接的修改元组
'''


tuple3[1][0] = "world"
print(tuple3)
# tuple1[-2] = "world"
# print(tuple1)


'''
删除元组：
del 元组名
元组是不可变的，因此没有清空元素的这些方法，
但是，我们可以通过del直接删除元组。
'''


'''
元组的连接：
元组3 = 元组1 + 元组2
功能：将元组1的元素与元组2的元素重新组合成一个新的元组并且返回
'''


t3 = tuple1 + tuple2
print(t3)


'''
元组的重复：
元组2 = 元组1*n
功能：将元组1的元素重复n次输出
'''


t4 = t3 * 2
print(t4)


'''
判断元素是否在元组中：
语法：
元素 in 元组
若存在于元组中，则返回True，否则返回False
'''


print(12 in t3)
print('12' in t3)


'''
元组的截取：
语法：
元组名[start:end]
start若不写，默认为0
end若不写，默认取到元组最后
若start和end都不写，则默认截取整个字符串
'''


str1 = "hello"
str2 = str1
str3 = str1[:]
print(str2 is str3) # True


t4 = t3
t5 = t3[:]
print(t4 is t5) # True


list1 = [1, 2, 3, 4]
list2 = list1
list3 = list1[:]
print(list2 is list3) # False
