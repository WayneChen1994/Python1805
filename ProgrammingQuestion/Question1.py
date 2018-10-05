#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author: Wayne.Chen

print("编程题".center(50, "="))

# 1、打印99乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         print("%dx%d=%d" % (j, i, i*j), end="\t")
#     print()


# 2、求可被17整除的所有三位数
# 解法一：
# for i in range(100, 1000):
#     if i % 17 == 0:
#         print(i)
# 解法二：
# for i in range(100, 1000)[2::17]:
#     print(i)


# 3、写一个程序，提示输入正整数X，然后计算从1到X连续整数的和
# num = int(input("请输入一个正整数："))
# sum = 0
# n = 1
# res_str = ""
# if num == 1:
#     print(num, "=",num)
# else:
#     while n <= num:
#         res_str += str(n) + " + "
#         sum += n
#         n += 1
#     res_str = res_str[:-3] + " = " + str(sum)
#     print(res_str)


# 4、改写上面的计算过程，循环嵌套计算连续的和
# num = int(input("请输入一个正整数："))
# if num == 1:
#     print("1 = 1")
# else:
#     x = 1
#     for z in range(num+1):
#         for i in range(x, num+1):
#             for j in range(x+1, num+1):
#                 if i < j and i+1 == j:
#                     print("%d + %d = %d" % (i,j,i+j))
#             break
#         x += 1


# 5、有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
# alist = [1,2,3,4]
# count = 0
# for b in alist:
#     for s in alist:
#         for g in alist:
#             if len(set([b,s,g])) == 3:
#                 print(100*b+10*s+g)
#                 count += 1
# print("count =", count)



# 6、企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，
# 从键盘输入当月利润I，求应发放奖金总数？

profit = int(input("请输入当月利润（万）："))
award = 0
if profit <= 10:
    award = profit * 1.1
elif 10 <= profit < 20:
    award = 10 * 0.1 + (profit - 10) * 1.075
elif 20 <= profit < 40:
    award = 20 + (profit - 20) * 1.05








# 7、一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 8、输入某年某月某日，判断这一天是这一年的第几天？
# 9、古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？
# 10、判断101-200之间有多少个素数，并输出所有素数。
# 11、打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153
#是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。