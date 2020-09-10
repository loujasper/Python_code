# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : udf_py.py
# @Author: Administrator
# @Date  : 20/09/02
# @Desc  :


import sys

for line in sys.stdin:
    line = line.strip()
    fname, lname = line.split(' ')
    l_name = lname.lower()
    print ('\t'.join([fname, str(l_name)]))

# SELECT TRANSFORM(stuff)
# USING 'script'
# AS thing1, thing2
#
# or
#
# SELECT TRANSFORM(stuff)
# USING 'script'
# AS (thing1 INT, thing2 INT)


# hive (iteblog)> add ARCHIVE /home/iteblog/anaconda2.tar.gz;
# hive (iteblog)> add file /tmp/iteblog.py;
# hive (iteblog)> select
#               >    TRANSFORM(data)
#               >    USING 'anaconda2.tar.gz/anaconda2/bin/python iteblog.py'
#               >    as (min_num)
#               > from test_a;