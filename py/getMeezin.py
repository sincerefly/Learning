#!/usr/bin/python
#encoding:utf-8
import time
import urllib
import sys
import requests
from bs4 import BeautifulSoup

def getPicId(num):

    # 返回双位的字符串
    if len(str(num)) == 1:
        return '0'+str(num)
    else:
        return str(num)


def saveMeez(img_list):

    num = 0
    count = len(img_list)
    for girlLink in img_list:

        timestamp = time.time()
        pic_num = getPicId(num)
        pic_postfix = girlLink.split('.')[-1]
        pic_name = str(timestamp)[0:10] + pic_num + '.' + pic_postfix
        urllib.urlretrieve(girlLink, './meez.in/'+ pic_name)

        num = num + 1

        print "-> (%s/%s) %s" % (str(num), str(count), girlLink)


def getMeez(url):

    r = requests.get(url)
    content = r.content

    soup = BeautifulSoup(content, "html.parser")
    con = soup.find_all('div', attrs={"class":"main-body"})

    urls = con[0].find_all('img')
    flag = 0

    img_list = []
    for u in urls:
        if flag == 0:
            imgUrl = u.get('src')
            flag = 1
        else:
            imgUrl = u.get('data-original')

        img_list.append(imgUrl)

    saveMeez(img_list)


def hasArticle(url):
    r = requests.head(url)
    status_code = r.status_code
    print "(%s/%s) %s %s" % (aid, MaxID, url, status_code)
    if status_code == 200:
        return True
    else:
        return False


if __name__ == "__main__":

    # 设置文章的最高ID
    StartID = int(sys.argv[1])
    MaxID = int(sys.argv[2])

    # 遍历有效的文章链接
    for aid in range(StartID, MaxID+StartID):
        url = 'http://www.meez.in/a/%s.html' % str(aid)
        if hasArticle(url):
            getMeez(url)
        else:
            continue
