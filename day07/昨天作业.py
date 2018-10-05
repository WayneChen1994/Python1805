# def lens(obj):
#     if type(obj) in [str, list, tuple]:
#         if len(obj) > 5:
#             return True
#         else:
#             return False
#     else:
#         print("类型有误")
# print(lens("123"))
# print(lens("123452"))


# def func(obj):
#     if type(obj) == str:
#         if " " in obj:
#             return True
#         else:
#             return False
#     elif type(obj) in [list, tuple]:
#         if "" in obj:
#             return True
#         else:
#             return False
#     else:
#         print("类型有误")

# print(func("111"))
# print(func("11 1"))
# print(func(["a","","b"]))


# def jiecheng(n):
#     n = abs(n)
#     ji = 1
#     for x in range(1, n + 1):
#         ji *= x

#     return ji

# print(jiecheng(5))
# print(jiecheng(6))
# print(jiecheng(-5))


# def yuebei(m, n):
#     m1 = m
#     n1 = n
#     while True:
#         r = m % n
#         m = n
#         n = r
#         if r == 0:
#             break
#         else:
#             continue
#     return m, m1 * n1 / m


# print(yuebei(3, 6))
# print(yuebei(3, 2))
# print(yuebei(6, 10))


# def maopao(l):
#     for i in range(len(l)):
#         for j in range(len(l) - i - 1):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]


# list1 = [33, 12, 99, 34, 56, 78, 90]
# maopao(list1)
# print(list1)