# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : createtable.py
# @Author: Administrator
# @Date  : 20/08/31
# @Desc  :

import os
import sys
import re
import xlrd

# 检验是否全是英文字符

def hiveddl(excel_name):
    # 打开excel
    data = xlrd.open_workbook(excel_name)
    # 列出所有sheet
    list_sheet = data.sheet_names()
    filename = 'HiveDDL.txt'
    with open(filename, 'w', encoding="utf-8") as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        for sheet in list_sheet:
            sheet_index = data.sheet_by_name(sheet)
            row_cnt = sheet_index.nrows

            table_ch_name = sheet_index.cell(0, 1).value
            # 英文表名
            table_eg_name = sheet_index.cell(1, 1).value
            # 中文字段 返回数组
            ch_fields = sheet_index.col_values(2, 4)
            # print(ch_fields)
            # print(row_cnt)

            fields_count = len(ch_fields)
            print(fields_count)

            sql = "CREATE TABLE IF NOT EXISTS " + table_eg_name + "(\n"
            # 根据excel表格横纵坐标，注意从0开始，获取第一个字段 因为第一个字段前没有逗号，所以单独定义，再拼接
            str_colums = '{:<31}'.format(sheet_index.cell(4, 1).value) + '{:<10}'.format(sheet_index.cell(4, 3).value) \
                         + '{:<}'.format('COMMENT\'') + \
                         '{:<}'.format(sheet_index.cell(4, 2).value) + '\'\n'

            # 从第五行开始循环
            for i in range(5,4 + fields_count):
                str_colums += ',' + '{:<30}'.format(sheet_index.cell(i , 1).value) + '{:<10}'.format(sheet_index.cell(i, 3).value) \
                              + '{:<}'.format('COMMENT\'') + \
                              '{:<}'.format(sheet_index.cell(i, 2).value) + '\'\n'
            sql += str_colums
            sql += ') \n COMMENT \'' \
                   + table_ch_name \
                   + '\'\nPARTITIONED BY(pday STRING)' \
                     '\nROW FORMAT DELIMIETED ' \
                     '\n  FIELDS TERMINATED BY \'\\t\' ' \
                     '\nSTORED AS INPUTFORMAT' \
                     '\n \'org.apache.hadoop.mapred.TextInputFormat\'' \
                     '\nOUTPUTFORMAT' \
                     '\n \'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat\';\n \n \n \n'



        # print(sql)
            f.write(sql)


    f.close()







if __name__ == '__main__':
    excel_name = "E:\Python_code\com\python\code\create_table\example.xlsx"
    table_sql_dict = hiveddl(excel_name)
