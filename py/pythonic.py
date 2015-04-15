#!/bin/python
#encoding:utf-8
# 题目来自Pythontip 部分答案也整理自此

# List排序
l = [2, 8, 3, 50]
l.sort()
print l
print '------'

# 字符串逆序
s = '12345'
print s[::-1]
print '------'

# 输出字典key
# 一字典d，如d={1:'one', 2:'two', 3:'three'}
# 输出字典d的key，以','链接，如‘1,2,3'
d = {1: 'one', 2: 'two', 3: 'three'}
print ','.join([str(key) for key in d.keys()])
print '------'

# 输出字符奇数位置的字符串
# 一个字符串 a， 输出字符奇数位置的字符串
# 如a=‘12345’，则输出135
a = '12345'
print a[::2]
print '------'














