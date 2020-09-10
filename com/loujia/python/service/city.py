# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : city.py
# @Author: Administrator
# @Date  : 20/09/10
# @Desc  :
from dao.getdata import GetData

class Analysis:
    """
    解析数据
    """
    @staticmethod
    def analysis(sql):
        results = []
        db = GetData()
        aa = db.Select(sql)
        print(len(aa))
        for row in aa:
            date = row[0]
            area = row[1]
            city = row[2]
            adid = row[3]
            count = row[4]
            if row[4] < 100:
                continue
            else:
                results.append(row)
            #循环写出
            #resultdata = '{0}\t{1}\t{2}\t{3}\t{4}\n'.format(date,area,city,adid,count)
        return results


if __name__ == '__main__':
    ana = Analysis()
    sql = "select * from area_city_ad_count;"
    data = ana.analysis(sql)
    print(data)