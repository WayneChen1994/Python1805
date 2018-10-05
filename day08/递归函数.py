'''
递归函数：
在函数体的内部，我们可以调用其他函数，
但当调用的这个函数是我们函数体本身的时候，我们称这个函数为递归函数
'''

'''
方法：
1、找出临界值
2、找出这一次与上一次的关系
3、找出结果与结果之间的关系
'''

'''
使用递归来实现：
1+2+3+100

f(1) --> 1
f(2) --> 1+2 --> f(1)+2
f(3) --> 1+2+3 --> f(1)+f(2)+3
……
f(100) --> 100+ f(99)
f(99) --> 99 + f(98)
'''


def f(n=100):
    if n == 1:
        return 1
    else:
        return n + f(n - 1)


# print(f())
# print(f(998))

'''
使用递归实现n!
f(1) 1
f(2) f(1) *2
f(3) f(1)*f(2)*3
'''


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(3))


'''
斐波那契数列：
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610……
求第n个数字上的数值
'''


def feibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return feibo(n - 2) + feibo(n - 1)


print(feibo(9))

'''
递归优点：
定义简单，逻辑清晰
'''


def feibo2(n):
    pre = 1
    cur = 1
    li = [pre, cur]
    nex = pre + cur
    for i in range(n - 2):
        li.append(nex)
        pre = cur
        cur = nex
        nex = pre + cur
    print("斐波那契数列：", li)
    return li[n - 1]


print(feibo2(12))
