# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : getDataBaseLink.py
# @Author: Administrator
# @Date  : 20/09/05
# @Desc  :
from thrift.transport import TSocket
from thrift.protocol import TCompactProtocol
from thrift.transport.TTransport import TFramedTransport
from impala.dbapi import connect
import sys
import errno
import os
import socket
import struct
import sys

from impala.util import as_pandas
def getdata():
    conn = connect(host='hadoop102',
                           port=10000,
                           auth_mechanism="PLAIN",user="root",password="123456",
                           database="default"
                   ,protocol ="compact"
                   # ,autoconnect=True,timeout=None
                   )

    cursor = conn.cursor()

    cursor.execute("show tables;")

    print(as_pandas(cursor))

    cursor.close()
    conn.close()
getdata()
