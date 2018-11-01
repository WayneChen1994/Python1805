#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


from pymongo import MongoClient


client = MongoClient()
db = client.studb
stu = db.stu


# 删除名字以数字结束的女生记录
# $regex正则支持\d
stu.remove({"sex":0, "name":{"$regex":"\d$"}})


client.close()
