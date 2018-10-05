'''
def insertSort(lists):
    for i in range(len(lists)):
        p = i
        while p > 0:
            if lists[p] < lists[p - 1]:
                lists[p], lists[p - 1] = lists[p - 1], lists[p]
            p -= 1
    return lists


print(insertSort([34, 23, 12, 45, 31, 6, 41, 73, 25]))
'''


def f(x, l=[]):
    print("for循环外的l：", l)
    print("l的地址：", id(l))
    for i in range(x):
        l.append(i * i)
        print("for循环内的l：", l)
    print("结果：", l)


f(2)
print("f(2)执行结束")
f(3, [3, 2, 1])
print("f(3,[3,2,1])执行结束")
f(3)
print("f(3)执行结束")
f(4)
