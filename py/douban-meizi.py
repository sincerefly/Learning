#encoding:utf-8
from bs4 import BeautifulSoup
from urllib.error import URLError,HTTPError
import os,socket
import urllib.request
#创建文件夹
path = os.getcwd();
new_path = os.path.join(path,"豆瓣妹子")
if not os.path.exists(new_path):
    os.mkdir(new_path)

#先访问下主页，获得总页数,cgidata.page_count=370;,这个cgidata.page_count保存的是总页数
HomeUrl = 'http://www.dbmeizi.com'
try:
    content = urllib.request.urlopen('http://www.dbmeizi.com',timeout=20).read().decode('utf-8')
except socket.timeout as e:
    print('网速太慢，重新运行试试看！')
    #print(content)

index_begin = content.find('cgidata.page_count=')
index_begin += len('cgidata.page_count=')
index_end = content.find(';',index_begin)
PageCount = content[index_begin:index_end]#截取的总页数
nPageCount = int(PageCount,10)
print(nPageCount)

#循环访问页面下载图片
#页面的地址格式http://www.dbmeizi.com/?p=0
for page in range(nPageCount):
    print('正在下载第%d页'%page)
    Pageurl='http://www.dbmeizi.com/?p=%d' %page
    try:
        content_1=urllib.request.urlopen(Pageurl,timeout=20).read().decode('utf-8')
    except:
        continue #出现异常跳到下一页
    soup = BeautifulSoup(content_1)
    picUrls= soup.find_all('img')
    for girlUrl in picUrls:
        if girlUrl.get('src'):
            #girlLink =  'http:'+girlUrl.get('src')
            girlLink =  girlUrl.get('src')
            print(girlLink)
        else:
            continue
        try:
            #import pdb; pdb.set_trace();
            content_2 = urllib.request.urlopen(girlLink,timeout=5).read()
            f = open('豆瓣妹子//'+girlLink[-15:],'wb')
            f.write(content_2)
        except:
            continue #这里出现任何的异常就跳过下载下一张图片
print('下载完毕！按任意键退出~~')
input()


