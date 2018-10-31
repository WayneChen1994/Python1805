#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import pymysql


db = pymysql.connect("127.0.0.1", "root", "0831", "studb")
cursor = db.cursor()


sql = "delete from stutable where age<19"


try:
    cursor.execute(sql)
    db.commit()
except Exception as e:
    print(e)
    db.rollback()


db.close()
