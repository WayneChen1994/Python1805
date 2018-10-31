#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


import pymysql


db = pymysql.connect("127.0.0.1", "root", "0831", "studb")
cursor = db.cursor()


sql = "create table teacher(" \
      "id int not null auto_increment primary key," \
      "name varchar(20) not null," \
      "age int not null)"


cursor.execute(sql)
res = cursor.fetchone()
print(res)
db.close()
