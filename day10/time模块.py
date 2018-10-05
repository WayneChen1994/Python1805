'''
时间戳：从1970年1月1日凌晨直到现在所经历的时间，以秒为单位来进行表示。【唯一标识】
UTC：格林尼治时间【UTC+8】
DST：夏令时，夏季调快1小时
'''

'''
总结：
时间元组
tm_year=2018,【年】
tm_mon=9,【月】
tm_mday=26,【日】
tm_hour=0,【时】
tm_min=0,【分】
tm_sec=0,【秒】
tm_wday=2,【星期码】
tm_yday=269,【日期，天数】
tm_isdst=-1【标识，计时方式】

时间字符串格式化
%Y：年
%m：月
%d：日
%X：时分秒 == %H:%M:%S
%H：时
%M：分
%S：秒

星期码：
0～6:0星期一，6星期日
'''

import time

t1 = time.time()
print(t1)

# 获取格林尼治时间
gt = time.gmtime(t1)
print(gt)
# 星期码/日期码 0~6， 0：星期一 6：星期日

# 获取本地时间
lt = time.localtime(t1)
print(lt)

# 使用此方法将时间元组转为时间字符串
asct = time.asctime(lt)
print(asct)

# 格式化时间元组
# 参数一：格式化字符串
# 参数二：被格式化的时间元组
strft = time.strftime('%Y-%m-%d %H:%M:%S', lt)
strft2 = time.strftime('%Y-%m-%d %X', lt)
strft3 = time.strftime('%Y-%m-%d', lt)
strft4 = time.strftime('%X', lt)
print(strft)
print(strft2)
print(strft3)
print(strft4)

# 时间元组转为时间戳
t2 = time.mktime(gt)
t3 = time.mktime(lt)
print(t2)
print(t3)

# 将时间字符串转为时间元组
t5 = time.strptime('2018-9-26', '%Y-%m-%d')
print(t5)
t6 = time.mktime(t5)
print(t6)

# 初始值
print(time.clock())
time.sleep(2)
time1 = time.clock()

print("********")
time.sleep(2)
time2 = time.clock()

print(time1)
print(time2-time1)
