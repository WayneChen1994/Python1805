'''
1.有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

list1 = []
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            # x、y、z互不相等的简写形式
            if x != y != z != x:
                list1.append(x * 100 + y * 10 + z)
print(list1)
print(len(list1))

'''


'''
2.企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提成10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时

def func2(p):
    res = 0
    profits = [1000000, 600000, 400000, 200000, 100000, 0]
    awards = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    for i in range(6):
        if p > profits[i]:
            # 得到当前阶段超出的部分
            out = p - profits[i]
            # 累加当前阶段所对应的奖金
            res += out * awards[i]
            # 因为当前阶段的奖金已累加完，要把利润重新赋值，不然会重复累加奖金
            p = profits[i]
    return res


yourProfit = int(input("请输入当月利润（元）："))
print("应发奖金总数为：%d元" % func2(yourProfit))

'''


'''
3.【递归】斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：1、1、2、3、5、8、13、21、34、……。

def func3(n):
    if n < 2:
        return 1
    else:
        return func3(n - 2) + func3(n - 1)


print(func3(7))

'''


'''
4.将一个列表的数据复制到另一个列表中。

list4 = [1, 2, 3, 4, 5]
# newList4 = list4.copy()
newList4 = []
newList4.extend(list4)
print(newList4)

'''


'''
5.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

def func5(astr):
    eng = 0
    space = 0
    number = 0
    other = 0
    for char in astr:
        if char.isalpha():
            eng += 1
        elif char.isspace():
            space += 1
        elif char.isdigit():
            number += 1
        else:
            other += 1
    return eng, space, number, other


inputStr = input("请输入一行字符：")
eNum, sNum, nNum, oNum = func5(inputStr)
print("英文字母%d个，空格%d个，数字%d个，其他%d个" % (eNum, sNum, nNum, oNum))

'''


'''
7.【递归】有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

def func7(n):
    if n == 1:
        return 10
    else:
        return func7(n - 1) + 2


for i in range(5, 0, -1):
    print("第%d个人%d岁" % (i, func7(i)))

'''


'''
8.写代码，有如下列表，请按照功能要求实现每一个功能
li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
a.请输出"Kelly"
b.找到 'all'元素并将其修改为"ALL"

li = ["hello", 'seven', ["mon", ["h", "kelly"], 'all'], 123, 446]
print(li[2][1][1])
li[2][2] = li[2][2].upper()
print(li)

'''


'''
9.一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

for x in range(1, 1001):
    sum = 0
    for y in range(1, x):
        if x % y == 0:
            sum += y
    if x == sum:
        print(x)

'''


'''
10.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

def fun10(n):   # 返回该球第n次反弹的高度
    if n == 0:
        return 100
    else:
        return fun10(n - 1) / 2


def func10(n):  # 返回第n次落地时，共经过的米数
    if n == 1:
        return 100
    else:
        return func10(n - 1) + fun10(n - 1) * 2


print("第10次落地共经过：", func10(10), end="米\n")
print("第10次反弹的高度：", fun10(10), end="米\n")

'''


'''
11.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少?

def func11(n):
    if n == 10:
        return 1
    else:
        return (func11(n + 1) + 1) * 2


for i in range(1, 11):
    print("第%d天剩余的桃子数：%d" % (i, func11(i)))

'''


'''
猜数字

很多人在聚餐时都玩过猜数字游戏，由某人随机出一个指定范围内的数，然后其他人一个一个猜，猜的过程中区间不断缩小，直到猜中为止。

这里的猜数字游戏就是用程序来代替那个出数字的人，程序算法设计为：

1.输入数字区间--->2.系统产生区间内的随机数--->3.玩家输入自己猜的数字--->4.比较玩家猜的与答案的高低并提示--->5.未猜中则回到3，猜中则提示猜次数
'''
import random
import time

while True:
    print("猜数字游戏开始".center(50, "*"))
    time.sleep(1)
    start = int(input("请输入起始数字："))
    end = int(input("请输入结束数字："))
    print("系统产生区间[%d,%d]内的随机数---" % (start, end))
    time.sleep(1)
    sysNum = random.randint(start, end)
    print(" (～￣▽￣)～ 作弊码：%d ".center(50, "=") % sysNum)
    time.sleep(1)
    count = 0
    while True:
        yourNum = int(input("请输入猜测的数字："))
        count += 1
        if yourNum < sysNum:
            time.sleep(1)
            print(" ~(-_-|||~ 猜的数比答案小～")
        elif yourNum > sysNum:
            time.sleep(1)
            print(" ~(-_-|||~ 猜的数比答案大～")
        else:
            time.sleep(1)
            print(" o(*￣︶￣*)o 恭喜你猜中了！你一共猜了%d次～" % count)
            break
    sel = input("是否继续玩猜数字游戏？（yes/no）")
    if sel == "no":
        time.sleep(1)
        print(" (。・_・)/~~~ 拜拜，欢迎下次光临～")
        break
    elif sel == "yes":
        continue
