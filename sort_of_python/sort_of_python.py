# 冒泡排序
def buddle_sort(blist):
    length = len(blist)
    for i in range(length):
        for j in range(length-i-1):
            if blist[j] > blist[j+1]:
                blist[j], blist[j+1] = blist[j+1], blist[j]
    return blist


list1 = [23, 14, 56, 31, 7, 12, 46, 61, 22, 16]
# print(buddle_sort(list1))


# 插入排序
def insert_sort(ilist=[]):
    length = len(ilist)
    for i in range(length):
        for j in range(i):
            if ilist[j] > ilist[i]:
                ilist.insert(j, ilist.pop(i))
    return ilist


# print(insert_sort(list1))


# 希尔排序 - 分组插入排序
def shell_sort(slist):
    length = len(slist)
    group = length // 2
    while group >= 1:
        for i in range(group, length):
            j = i
            while(j - group) >= 0:
                if slist[j] < slist[j - group]:
                    slist[j], slist[j - group] = slist[j - group], slist[j]
                    j -= group
                else:
                    break
        group //= 2
    return slist


print(shell_sort(list1))

# 快速排序
# 直接选择排序
# 堆排序
# 归并排序
# 基数排序
