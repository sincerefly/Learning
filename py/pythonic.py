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

# 求解100以内的所有素数
# 输出100以内的所有素数，素数之间以一个空格区分
print ' '.join(['%s' % x for x in range(2,100) if not [y for y in range(2,x/2+1) if x % y == 0]])

alist = []
for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        alist.append(i)

print ' '.join(str(i) for i in alist)

def getPrime(maxNum):
    aList = [x for x in range(0,maxNum)]
    prime = []
    for i in range(2,len(aList)):
        if aList[i] != 0:
            prime.append(aList[i])
            clear(aList[i],aList,maxNum)
    return prime

def clear(aPrime,aList,maxNum):
    for i in range(2,int((maxNum/aPrime)+1)):
        if not aPrime*i>maxNum-1:
            aList[i*aPrime]=0

print ' '.join(str(i) for i in getPrime(100))

print '------'

# 最大公约数
# 两个正整数a和b， 输出它们的最大公约数
a = 10
b = 25

while b:
    a, b = b, a%b
print a

a = 10
b = 25

gcd = lambda x,y: gcd(y,x) if x < y else gcd(y,x%y) if x%y else y
print gcd(a,b)

a = 10
b = 25

if(b>a):
    a, b = b, a
while(b!=0):
    c=b
    b=a%b
    a=c
print(a)

a = 10
b = 25

def gcd(big,small):
    remainder = big % small #求余数
    if remainder == 0:   #如果两个数相除,余数为0，那么除数就是最大公约数了
        print small
    else:
        gcd(small,remainder) #调用gcd函数，带入最小的数(在这里也就是除数)和余数继续辗转相除运算，（两个数相除，除数肯定大于余数）

#接下来就是判断a和b谁的值大，因为求最大公约数是用大值除以小值
if a > b:
    gcd(a,b)
else:
    gcd(b,a)

print '------'

# 最小公倍数
# 两个正整数a和b， 输出它们的最小公倍数
a = 10
b = 25
def gcd(x, y):
    while y:
        x, y = y, x%y
    return x
print a*b/gcd(a, b)























