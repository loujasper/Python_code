# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : parse_json2.py
# @Author: Administrator
# @Date  : 20/09/11
# @Desc  :
import json
"""
#样例数据
{
  "mindata": {
    "sign": "AKD239DFJ3ASDKFJH34",
    "header": {
      "resp_time": "2019-03-20 16:25:12",
      "res_msg": "操作成功",
      "version": "4.0",
      "ret_code": "0000000",
      "req_time": "2019-03-20 15:29:23"
    },
    "body": {
      "user_features": [
        {
          "user_features_type": "0",
          "last_modified_date": "2010-49:10 13:29:13"
        }
      ],
      "last_modified_time": "2018-49:10 13:29:13",
      "id_detail": {
        "birthday": "1993-03-20",
        "address": "19287492824",
        "name": "张三",
        "gender": "男",
        "id_number_mask": "21448321034273402",
        "nation": "汉",
        "name_credible": "张三",
        "issuing_agency": "你好"
      }
    }
  }
}
"""

with open("C:\\Users\\lenovo\\Desktop\\operator.json",'r',encoding="utf8") as f:
    load_dict = json.load(f)

def parse_json(data):
    if data == None or data == "":
        pass
    results = []
    #第一层
    for item in data:
        #第二层
        for j in data[item]:

            #在第二层中判断是否是dict 如果不是直接append
            if isinstance(data[item][j], dict):
                dict1 = data[item][j]

                #第三层循环
                for x in dict1:
                    #获取到list格式数据
                    if isinstance(dict1[x],list):
                        #print(dict1[x][0])
                        liststr = dict1[x][0]
                        #循环列表中的每一个dict
                        for list1 in liststr:
                            results.append(liststr[list1])

                    #获取到字典格式数据
                    elif isinstance(dict1[x],dict):
                        d = dict1[x]
                        for it in d:
                            results.append(d[it])

                    else:
                        results.append(dict1[x])
            else:
                results.append(data[item][j])

        return results


def writeFile():
    data = parse_json(load_dict)
    writeFile = open('channel_filter_data.txt', 'w', encoding='utf-8')
    for row in data:
        #print(row)
        writeFile.write(row+"\t")


writeFile()