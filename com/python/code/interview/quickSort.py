# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : quickSort.py
# @Author: Administrator
# @Date  : 20/09/02
# @Desc  :
myList = [7, 6, 5, 3, 12, 20, 1, 9, 11, 4, 15, 10, 8]

def quickSort(myList, start, end):
    # 判断start是否小于end,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = myList[i]

        while i < j:
            # 如果列表后边的数比基准数大或相等,则前移一位直到有比基准数小的数
            while (i < j) and (myList[j] >= base):
                j = j - 1

            # 如找到,则把第j个元素赋值给第i个元素
            myList[i] = myList[j]

            # 同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j，此时找到基准值
        myList[i] = base

        # 递归前后半区
        # print(base, myList)
        quickSort(myList, start, i - 1)
        quickSort(myList, j + 1, end)
    return myList



print("myList:", quickSort(myList, 0, len(myList) - 1))