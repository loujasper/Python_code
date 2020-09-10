# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : db_handle.py
# @Author: Administrator
# @Date  : 20/09/08
# @Desc  :
import pymysql
from Utils.ConfigHandler import ConfigParse

class DB(object):

    def __init__(self):
        """
        初始化数据库连接
        """
        self.db_conf = ConfigParse.get_db_config()
        self.conn = pymysql.connect(
            host = self.db_conf['host'],
            port = int(self.db_conf['port']),
            user = self.db_conf['user'],
            passwd = self.db_conf['passwd'],
            database = self.db_conf['database'],
            charset = self.db_conf['charset']
        )
        self.cur =self.conn.cursor()


    def CloseConnect(self):
        """
        提交，然后关闭游标和数据库连接
        :return:
        """
        #提交
        self.conn.commit()
        #关闭游标
        self.cur.close()
        #关闭连接
        self.conn.close()


    def Excute(self, sql):
        """
        执行SQL语句
        :param sql: 输入一段SQL
        :return: 返回结果数据
        """
        try:
            self.cur.execute(sql)
            self.conn.commit()
            # resultdata = self.cur.fetchall()
            # # for row in resultdata:
            # #     result.append(row)
            # return resultdata
        except Exception as e:
            print("SQL execute fail：",sql,e)


# if __name__ == '__main__':
    # db =DB()
    # print(db.Excute("select * from area_city_ad_count"))