# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : getdata.py
# @Author: Administrator
# @Date  : 20/09/08
# @Desc  :
from Utils.db_handle import DB

class GetData:
    @staticmethod
    def Select(sql):
        """
        执行SQL语句
        :return: 返回SQL查询结果
        """
        db = DB()
        try:
            cur = db.cur
            cur.execute(sql)
            results = cur.fetchall()
            return results
        except Exception as e:
            print("SQL Select Fail：",sql,e)

        db.CloseConnect()


