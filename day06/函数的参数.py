'''
函数参数的作用：
在实际项目中，有时候有些未知选项【可变选项】要参与运算，我们就可以通过函数的参数来实现
形式参数【形参】：在函数中的参数列表中定义的，作为一个中间值来接收参数的，我们称之为形参
实际参数【实参】：在函数调用的时候，传递的参数，要参与运算的参数，我们称之为实参。
'''


def sum1(n):
    res = 0
    for x in range(1, n + 1):
        res += x
    return res


print(sum1(100))

'''
注意：参数的传递，实际上就是实参给形参赋值的过程
'''

'''
需求：使用函数求m+……+n的和【m,n】区间的所有数之和
'''


def sum2(m, n):
    if m > n:
        m, n = n, m
    res = 0
    for x in range(m, n + 1):
        res += x
    return res


print(sum2(0, 10))
print(sum2(10, 0))
print(sum2(10, 10))

'''
使用函数
传递一个字符串，分别统计出英文字母、空格、数字和其他字符的个数并返回
'''


def myCount(astr):
    spaceNum = 0
    alphaNum = 0
    NumberNum = 0
    otherNum = 0
    for char in astr:
        if char.isspace():
            spaceNum += 1
        elif char.isdecimal():
            NumberNum += 1
        elif char.isalpha():
            alphaNum += 1
        else:
            otherNum += 1
    return alphaNum, spaceNum, NumberNum, otherNum


print(myCount("^&*Hello, World 1 2 3!#*"))
