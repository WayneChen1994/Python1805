'''
偏函数：
概念：偏函数就是将函数的某些参数固定住，把函数的调用变得更加简单，类似于某些函数中设置默认参数
'''

'''
偏函数的使用：
偏函数是functools模块提供的，因此，我们首先需要导入functools模块
语法：
functools.partial(函数名，要固定的参数)
'''
import functools
import operator


int3 = functools.partial(int, base=2)
# print(int3("1010"))

# print(int("1010", base=2))


def int2(string):
    return int(string, base=2)


# print(int2("1010"))
# print(int2("10110"))
# print(int2("10101"))

'''
需求：随机输入一个数，求这个数与100比，输出最大的那个
用偏函数实现
'''
max2 = functools.partial(max, 100)
# print(max2(102, 89))
# print(max2(99))


def func(a, b):
    return a + b


'''
返回任何数与10相加的值
'''
func2 = functools.partial(func, 10)
func3 = functools.partial(func, b=10)
# print(func2(120))
# print(func2(10))
# print(func3(100))

add2 = functools.partial(operator.add, 100)
print(add2(100))
print(add2(10))
