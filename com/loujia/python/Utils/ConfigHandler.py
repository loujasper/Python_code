# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : ConfigHandler.py
# @Author: Administrator
# @Date  : 20/09/06
# @Desc  :

from configparser import ConfigParser
from config.public import config_path

class ConfigParse(object):
    def __init__(self):
        pass

    @classmethod
    def get_db_config(cls):#使用类方法，cls就是指定本身

        cls.cfp = ConfigParser()
        cls.cfp.read(config_path) #读取配置文件目录
        host = cls.cfp.get("sparksql","host")
        port = cls.cfp.get("sparksql", "port")
        user = cls.cfp.get("sparksql", "user")
        passwd = cls.cfp.get("sparksql", "passwd")
        database = cls.cfp.get("sparksql", "database")
        charset = cls.cfp.get("sparksql", "charset")

        return {"host": host, "port": port, "user": user, "passwd": passwd, "database": database, "charset": charset}

if __name__== "__main__":
    cp = ConfigParse()
    print(cp.get_db_config())

















