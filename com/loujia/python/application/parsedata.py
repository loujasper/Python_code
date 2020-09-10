# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : parsedata.py
# @Author: Administrator
# @Date  : 20/09/06
# @Desc  :
import configparser
# 读取配置文件
db_cfg = configparser.RawConfigParser().read("getData")
from Utils import ConfigHandler

def parseData(sql):
    db = ConfigHandler.DBHelper(sql, params=None)
    db.Execute()
    db.ConnectionDatabase()
    data = db.Select()
    for row in data:
        print(row)
    db.Close()



if __name__ == '__main__':
    sql = "select * from area_city_ad_count"
    parseData(sql)