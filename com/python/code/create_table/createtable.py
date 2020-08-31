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
            # 因为表的字段信息都是放在01、02这种sheet的，所以正则匹配
            patten = "\d+"
            flag = re.match(patten, sheet)
            if flag:
                sheet_index = data.sheet_by_name(sheet)

                row_cnt = sheet_index.nrows
                # 中文表名
                table_ch_name = sheet_index.cell(0, 1).value
                # 英文表名
                table_eg_name = sheet_index.cell(1, 1).value
                # 中文字段
                ch_fields = sheet_index.col_values(1, 6)
                # print(ch_fields)
                # 字段行数
                field_count = len(ch_fields)

                sql = "CREATE TABLE IF NOT EXISTS " + table_eg_name + "(\n"
                str_colums = '{:<31}'.format(sheet_index.cell(4, 2).value) + '{:<10}'.format('STRING') \
                             + '{:<}'.format('COMMENT\'') + \
                             '{:<}'.format(sheet_index.cell(4, 2).value) + '\'\n'
                # print(str_colums)
                # 因为字段是从第7行开始，所以从第7行开始循环
                for i in range(6, field_count):
                    str_colums += ',' + '{:<30}'.format(sheet_index.cell(i + 1, 2).value) + '{:<10}'.format('STRING') \
                                  + '{:<}'.format('COMMENT\'') + \
                                  '{:<}'.format(sheet_index.cell(i + 1, 1).value) + '\'\n'
                sql += str_colums

                sql += ') \n COMMENT \'' \
                       + table_ch_name \
                       + '\'\nPARTITIONED BY(pday STRING)' \
                         '\nROW FORMAT DELIMIETED ' \
                         '\n  FIELDS TERMINATED BY \'\\t\' ' \
                         '\nSTORED AS INPUTFORMAT' \
                         '\n \'org.apache.hadoop.mapred.TextInputFormat\'' \
                         '\nOUTPUTFORMAT' \
                         '\n \'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat\';\n'
                print(sql)

                f.write(sql)
    f.close()


def mysqlddl(excel_name):
    # 打开excel
    data = xlrd.open_workbook(excel_name)
    # 列出所有sheet
    list_sheet = data.sheet_names()
    filename = 'MysqlDDL.txt'
    with open(filename, 'w', encoding="utf-8") as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
        for sheet in list_sheet:
            # 因为表的字段信息都是放在01、02这种sheet的，所以正则匹配
            patten = "\d+"
            flag = re.match(patten, sheet)
            if flag:
                sheet_index = data.sheet_by_name(sheet)
                row_cnt = sheet_index.nrows

                # 英文表名
                table_eg_name = sheet_index.cell(1, 1).value
                # 中文字段
                ch_fields = sheet_index.col_values(1, 6)
                # print(ch_fields)
                # 字段行数
                field_count = len(ch_fields)

                sql = "CREATE TABLE IF NOT EXISTS " + table_eg_name + "(\n"
                str_colums = '{:<31}'.format('id') + '{:<30}'.format('INT NOT NULL AUTO_INCREMENT') \
                             + '{:<}'.format('COMMENT\'') + \
                             '{:<}'.format('ID') + '\'\n'
                # print(str_colums)
                # 因为字段是从第7行开始，所以从第7行开始循环
                for i in range(6, field_count):
                    is_blank_cell = sheet_index.cell(i + 1, 4).value
                    is_blank = lambda cell: 'NOT NULL' if is_blank_cell == '是' else ""
                    str_colums += ',' + '{:<30}'.format(sheet_index.cell(i + 1, 2).value) \
                                  + '{:<20}'.format(sheet_index.cell(i + 1, 3).value) \
                                  + '{:<15}'.format(is_blank(is_blank_cell)) \
                                  + '{:<}'.format('COMMENT\'') \
                                  + '{:<}'.format(sheet_index.cell(i + 1, 1).value) + '\'\n'
                sql += str_colums

                sql += ',PRIMARY KEY (id) \n ' \
                       ') ENGINE=InnoDB  DEFAULT CHARSET=utf8 COMMENT=\'' + format(
                    sheet_index.cell(0, 1).value) + '\';\n'
                print(sql)

                f.write(sql)
    f.close()


if __name__ == '__main__':
    excel_name = "C:\\Users\\yangxiaofeng\\Desktop\\天津应急明细层v0.1_20200415.xls"
    hiveddl(excel_name)
    mysqlddl(excel_name)