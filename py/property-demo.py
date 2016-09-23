#!/bin/env python
# -*- coding: utf-8 -*-


# ------------------------------------------------------------------------
# 可以使用property对类添加额外的属性，来扩展函数的功能
# 如下Person类所示，不过想要修改值，需要间接修改first_name, last_name实现
# ------------------------------------------------------------------------

class Person(object):

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        print 'hello, %s %s' % (self.first_name, self.last_name)


p = Person('xiao', 'ming')
p.full_name    #  hello, xiao ming


# ------------------------------------------------------------------------
# 对属性进行校验
# 当需要对属性在获取或者赋值的同时，希望进行一些额外的操作，可以使用property
# 新建一个`name`内置方法，然后用装饰器@property修饰，那么可以使用@name.setter
# 支持通过赋值来修改变量的值
# 另外值得注意的是下边注释_name，是可以工作的，因为property在使用同名的变量后
# 将数据存储在了以下划线开头的_同名变量中
# 使用self.name = name可以使得初始化的时候也可以进行校验
# ------------------------------------------------------------------------

class Person2(object):
    def __init__(self, name):
        self.name = name
        #self._name = name

    @property
    def name(self):
        print self._name

    @name.setter
    def name(self, value):
        if value != 'gimp':
            self._name = value

p = Person2('xiao ming')
p.name                     # xiao ming
p.name = 'dongdong'
p.name                     # dongdong
p.name = 'gimp'
p.name                     # dongdong


# ------------------------------------------------------------------------
# 对于已经定义了获取属性，设置属性的类，可以使用如下方法来对属性进行控制
# 值得说明的是property后边的参数顺序是不能变的，获取/设置/删除(如果有的话)
# ------------------------------------------------------------------------


class Person3(object):
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print self._name

    def set_name(self, value):
        self._name = value

    name = property(get_name, set_name)


p = Person3('mr.liu')
p.name                 # mr.liu
p.name = 'mr.zhang'
p.name                 # mr.zhang








