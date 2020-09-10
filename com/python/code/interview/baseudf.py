#!/usr/bin/python3
# -- coding: utf-8 --
import logging
from pyhive.hive import connect
import pandas as pd

from sasl.saslwrapper import *

class HiveFetcher:
    def __init__(self,host="hadoop102", port=10000,
                 username="hadoop", auth="KERBEROS", database="default",
                 kerberos_service_name="hive"):
        self.host =host
        self.port =int(port)
        self.username=username
        self.auth=auth
        self.database=database
        self.kerberos_service_name = kerberos_service_name
        self.conn = None
        self.cur = None

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = connect(host=self.host, port=self.port, username=self.username,
                                     database=self.database, auth=self.auth,
                                     kerberos_service_name=self.kerberos_service_name)
        except Exception as e:
            print("connect hive Database failed:{}".format(e))
            return False
        self.cur = self.conn.cursor()
        return True


    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None):
        # 连接数据库
        self.connectDatabase()
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                self.cur.execute(sql, params)
                self.conn.commit()
        except:
            print("execute failed: " + sql)
            self.close()
            return False
        return True

    # 用来查询表数据
    def fetchall(self, sql):
        self.execute(sql)
        # print(aa)
        return self.cur

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

def orgindata_fetch(connect_type):

    search_data=()
    sql_search = 'select * from default.student2;'
    # 从数据库中查询相关数据
    print(sql_search)

    try:
        search_data = connect_type.fetchall(sql_search)
    except Exception as e:
        logging.error('连接hive数据库，执行提取原始数据操作出现故障:{}'.format(e), exc_info=True)
        search_data = pd.DataFrame(list(search_data))

    return search_data


print('开始读取数据...')
# if __name__ == '__main__':
hive_conns = HiveFetcher()

ori_data = orgindata_fetch(hive_conns)
print(ori_data)
    # print(ori_data)
# def get_data():
#     conn = hive.Connection(host='hadoop102', port=10000, username='hadoop', database='default',auth='NOSASL')#host主机ip,port：端口号，username:用户名，database:使用的数据库名称
#     cursor=conn.cursor()
#     cursor.execute("show tables")#执行查询
#     for result in cursor.fetchall():
#         print(result)
#
#     conn.close()
# if __name__ == '__main__':

    # get_data()