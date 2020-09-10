# !/usr/bin/python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: Administrator
# @Date  : 20/09/07
# @Desc  :


class Money:
    pass

# 一般对象可以修改__dict__属性，但类对象的__dict__为只读，默认无法修改，可通过setattr方法修改

one = Money()
one.age = 18

# print(one.__dict__)


# 方法和函数的区别
# 1.函数

def eat():
    print(1)
    print(2)
    print(3)
#调用方式
# eat()

# 方法
class Person:
    def eat2(self):
        print("这是一个实例方法, 默认第一参数需要接收到一个实例", self)


    @classmethod   #装饰器类方法
    def leifangfa(cls,a):
        print("这是一个类方法，默认第一参数是接收到一个类", cls,a)
    # 装饰器的作用：在保证原本函数不变的前提下，直接给这个函数添加一个功能。

    @staticmethod  #静态方法 @staticmethod是一个装饰器
    def jingtaifangfa():
        print("这是一个静态方法,第一个参数默认不接收")

# 实例  ---调用方式
p = Person()

# 类属性
print(p.jingtaifangfa())

# 实例属性
p.age = 3


#-----------------------------------------
# 类属性可以通过类去访问，也可以用实例去访问
# 但是实例属性只能通过实例去访问



# ----------------------------------------


# 继承：

class A(Person):
    pass

A.leifangfa(111)


def xxx():
    """
    这是一个方法
    :return:
    """
    print("xxx")
