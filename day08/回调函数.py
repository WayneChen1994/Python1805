'''
什么是回调函数？
简单来说，回调函数就是把一个函数作为参数传递到另一个函数中
'''

'''
同桌提供叫醒服务，time：
服务1、踢凳子
服务2、打耳巴子
服务3、叫醒
'''

'''
按钮的点击事件
'''


def fuwu1(t):
    print("使用踢凳子的方式在%s叫醒" % t)


def fuwu2(t):
    print("使用打耳巴子的方式在%s叫醒" % t)


def fuwu3(t):
    print("使用叫的方式在%s叫醒" % t)


def server(f, t):
    f(t)


server(fuwu2, "14:00:00")

# 装饰器


def outer(f):
    def inner():
        print("**********")
        f()
    return inner
