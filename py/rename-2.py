#!/bin/env python
#encoding:utf-8
import sys, string, os, shutil
#输入目录名和前缀名，重命名后的名称结构类似prefix_0001
def RenameFiles(srcdir, prefix):
    srcfiles = os.listdir(srcdir)
    index = 1
    for srcfile in srcfiles:
        srcfilename = os.path.splitext(srcfile)[0][1:]
        sufix = os.path.splitext(srcfile)[1]
		#根据目录下具体的文件数修改%号后的值，"%04d"最多支持9999
        destfile = srcdir + "//" + prefix + "_%04d"%(index) + sufix
        srcfile = os.path.join(srcdir, srcfile)
        os.rename(srcfile, destfile)
        index += 1
srcdir = "test"
prefix = "IMG_2015"
RenameFiles(srcdir, prefix)
