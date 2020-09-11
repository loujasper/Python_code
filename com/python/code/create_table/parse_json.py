# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : parse_json.py
# @Author: Administrator
# @Date  : 20/09/10
# @Desc  :
# C:\Users\lenovo\Desktop\operator.json

import pandas as pd
import json
import numpy as np

with open("C:\\Users\\lenovo\\Desktop\\operator.json",'r',encoding="utf8") as f:
    load_dict = json.load(f)
    # print(load_dict)

    load_dict = load_dict['mindata'] #拆除第一层花括号
    #print(load_dict)
    data_raw = pd.DataFrame(columns=load_dict.keys())
    #print(data_raw)
    data_raw = data_raw.append(load_dict, ignore_index=True)
    # print(data_raw)
    #print(data_raw)
#
### 对嵌套的json进行拆包，每次拆一层
def json_to_columns(df,col_name):
    for i in df[col_name][0].keys():         # 对dict的第一层key进行循环
        list2=[j[i] for j in df[col_name]]   # 存储对应上述key的value至列表推导式
        df[i]=list2                          # 存储到新的列中
    df.drop(col_name,axis=1,inplace=True)    # 删除原始列
    return df

#
# ### 遍历整个dataframe，处理所有值类型为dict的列
def json_parse(df):
    for i in df.keys():
        if type(df[i][0])==dict and df[i][0]!={}:
            df=json_to_columns(df,i)   #调用上面的函数
        return df

### 处理值类型为list的列，转换为dict
def list_parse(df):
    for i in df.keys():
        if type(df[i][0])==list and df[i][0]!=[]:
            list1=[j[0] if j!=[] else np.nan for j in df[i]]
            df[i]=list1
    return df
#



wrifile = open('channel_filter_data.txt','w',encoding='utf-8')
wrifile.write(str(json_parse(data_raw)))
wrifile.close()


data = { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
json = json.dumps(data)

def getjson(json_str,jsonarray=[]):
    for i in json_str:
        if isinstance(json_str, dict):
            print(i,json_str[i])

getjson(data)