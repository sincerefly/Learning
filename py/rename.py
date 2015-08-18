#!/usr/bin/env python
#encoding:utf-8
import os
import sys
import time

def getPicId(old_name, piclist):

    num = piclist.index(old_name)

    # 返回双位的字符串
    if len(str(num)) == 1:
        return '0'+str(num)
    else:
        return str(num)


def getTimeStamp():

    # 返回时间戳
    return time.time()


def getPiclist():

    # 获取当前目录下的图片列表
    filelist = os.listdir('./')
    piclist = [i for i in filelist if i != 'rename.py']

    return piclist


def rename():

    piclist = getPiclist()

    timestamp = getTimeStamp()

    for old_name in piclist:

        # 获取文章的id
        picid = getPicId(old_name, piclist)

        # 获取原文件后缀
        postfix = old_name.split('.')[1]

        # 文件新名称
        new_name = str(timestamp)[0:10] + picid + '.' + postfix

        # 构造命令并执行
        cmd = 'mv ' + old_name + ' ' + new_name
        os.system(cmd)


if __name__ == "__main__":

    rename()

