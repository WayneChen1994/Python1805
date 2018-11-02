#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


# 导入模块
import redis


# 参数一：ip地址
# 参数二：端口号，默认6379
# 参数三：数据库，默认0
# 参数四：密码，默认为None，若更改密码的情况下，需要添加密码
r = redis.StrictRedis(host='localhost', port=6379, db=0, password=None)


# 写入一条数据
r.set("name1", "lili")
print(r.get("name1").decode())


'''
若有多条数据需要设置的情况下，我们可以使用pipeline的方法
使用此方法，可以将我们的命令缓存起来，然后再执行execute的时候统一提交
'''


pipe = r.pipeline()
pipe.set("name2", "张三")
pipe.set("name3", "李四")
pipe.set("name4", "王五")
pipe.execute()


r.setex("name5", 20, "哈哈")
