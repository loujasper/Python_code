# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : public.py.py
# @Author: Administrator
# @Date  : 20/09/08
# @Desc  :
import os
# 获取项目的根目录的绝对路径
baseDir = os.path.dirname(os.path.dirname(__file__))
# 获取数据库配置文件
config_path = baseDir + "/config/dbConfig.ini"

# print(config_path)