#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：Wayne


'''
把数据操作封装为一个工具类
数据操作分为两大类：
1.插入、修改、删除，会造成数据库中的数据发生变化的，返回布尔值
2.查询结果，返回一个list，若没有查到返回None
'''

import pymysql


class DB():
    def __init__(self, user, psd, dbname, localhost="localhost", port=3306):
        self.localhost = localhost
        self.user = user
        self.psd = psd
        self.dbname = dbname
        self.port = port
        # 初始化的时候，获取到连接
        self.db = pymysql.connect(self.localhost, self.user, self.psd, self.dbname, self.port)
        # 通过打开的连接获取到游标
        self.cursor = self.db.cursor()

    '''
    执行sql语句
    插入、修改、删除，会造成数据库中的数据发生变化的，
    返回True，则代表执行成功
    返回False，则代表执行失败
    '''

    def excData(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except:
            self.db.rollback()
            return False

    # 获取一条数据
    def getOneData(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        if res:
            return res
        else:
            return None

    # 获取所有的数据
    def getAllData(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        if res:
            return list(res)
        else:
            return None

    # 获取数据条数
    def getDataNum(self, sql):
        self.cursor.execute(sql)
        return self.cursor.rowcount

    def insert(self, sql):
         return self.excData(sql)

    def update(self, sql):
        return self.excData(sql)

    def delete(self, sql):
        return self.excData(sql)


if __name__ == '__main__':
    db = DB("root", "0831", "studb")
    sql = "select * from stutable"
    # res = db.getAllData(sql)
    # for x in res:
    #     print(x[3]==b'\x00')
    # print(res)


    sql2 = "delete from stutable where age=19"
    res = db.excData(sql2)
    print(res)
