# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : parse_json2.py
# @Author: Administrator
# @Date  : 20/09/11
# @Desc  :
import json
import pandas as pd

with open("C:\\Users\\lenovo\\Desktop\\operator.json",'r',encoding="utf8") as f:
    load_dict = json.load(f)

## 获取 json 数组或json 对象的 key 列表
def get_json_keys(json_str,json_keys = []):
    if isinstance(json_str,list):
        for json_obj in json_str:
            #print(json_obj)
            for key in json_obj.keys():
                #print(key)
                if key not in json_keys:
                    json_keys.append(key)
    elif isinstance(json_str,dict):
        for key in json_str.keys():
                if key not in json_keys:
                    print(key)
                    json_keys.append(key)
    return json_keys

## 将json 数组中相同的 key - value值进行合并
def get_key_values(json_str,json_keys):
    target_json = {}
    for key in json_keys:
        key_values = []
        for json_obj in json_str:
            if isinstance(json_obj,dict):
                key_values.append(json_obj[key])
        target_json[key] = key_values
    return target_json

## 主方法
def analyse_json(json_str):
    target_json = {}
    json_keys = []
    if isinstance(json_str,list):
        json_keys = get_json_keys(json_str,json_keys)
        print(json_keys)
        target_json = get_key_values(json_str,json_keys)
    elif isinstance(json_str,dict):
        json_keys = get_json_keys(json_str,json_keys)
        for key in json_keys:
            if not isinstance(json_str[key],list) and not  isinstance(json_str[key],dict):
                target_json[key] = json_str[key]
            else:
                target_json[key] = analyse_json(json_str[key])
    return target_json


print(analyse_json(load_dict))


#print(analyse_json(d2))
# print(analyse_json(d3))