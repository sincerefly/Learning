#!/bin/env python
# coding=utf-8
import time
import urllib2
import re
import MySQLdb
import random

#######################################
# 这是一个从美使馆网站抓取pm2.5的小程序
# Useage:
#     ./get_pm25.py
# Date:
#     2014.12
#

# 过去当前日期
date = time.strftime("%Y-%m-%d", time.localtime(time.time()))
print "当前日期为：" + date

city_list = ['哈尔滨', '齐齐哈尔', '牡丹江', '长春', '吉林', '沈阳', '大连', '鞍山', '抚顺', '本溪', '丹东', '锦州', '盘锦', '葫芦岛', '北京', '天津', '上海', '重庆', '石家庄', '邯郸', '秦皇岛', '承德', '唐山', '保定', '张家口', '廊坊', '邢台', '衡水', '济南', '青岛', '威海', '烟台', '淄博', '枣庄', '东营', '潍坊', '济宁', '泰安', '日照', '莱芜', '临沂', '德州', '聊城', '滨州', '菏泽', '太原', '大同', '阳泉', '长治', '临汾', '西安', '铜川', '宝鸡', '咸阳', '延安', '郑州', '开封', '洛阳', '平顶山', '安阳', '焦作', '三门峡', '南京', '无锡', '徐州', '常州', '苏州', '南通', '连云港', '淮安', '盐城', '扬州', '镇江', '泰州', '宿迁', '合肥', '芜湖', '马鞍山', '黄山', '武汉', '荆州', '宜昌', '恩施', '杭州', '宁波', '温州', '嘉兴', '湖州', '绍兴', '金华', '衢州', '舟山', '台州', '丽水', '南昌', '景德镇', '九江', '长沙', '株洲', '湘潭', '岳阳', '常德', '张家界', '福州', '厦门', '泉州', '成都', '攀枝花', '泸州', '德阳', '绵阳', '宜宾', '南充', '自贡', '贵阳', '遵义', '昆明', '大理', '曲靖', '玉溪', '南宁', '桂林', '柳州', '北海', '广州', '深圳', '珠海', '汕头', '佛山', '韶关', '湛江', '茂名', '肇庆', '惠州', '梅州', '中山', '潮州', '东莞', '乌鲁木齐', '克拉玛依', '库尔勒', '海口', '三亚', '呼和浩特', '包头', '赤峰', '鄂尔多斯', '银川', '石嘴山', '西宁', '兰州', '嘉峪关', '拉萨', '香港', '澳门', '台北']

city_pinyin_list = ['haerbin', 'qiqihaer', 'mudanjiang', 'changchun', 'jilin', 'shenyang', 'dalian', 'anshan', 'fushun', 'benxi', 'dandong', 'jinzhou', 'panjin', 'huludao', 'beijing', 'tianjin', 'shanghai', 'zhongqing', 'shijiazhuang', 'handan', 'qinhuangdao', 'chengde', 'tangshan', 'baoding', 'zhangjiakou', 'langfang', 'xingtai', 'hengshui', 'jinan', 'qingdao', 'weihai', 'yantai', 'zibo', 'zaozhuang', 'dongying', 'weifang', 'jining', 'taian', 'rizhao', 'laiwu', 'linyi', 'dezhou', 'liaocheng', 'binzhou', 'heze', 'taiyuan', 'datong', 'yangquan', 'changzhi', 'linfen', 'xian', 'tongchuan', 'baoji', 'xianyang', 'yanan', 'zhengzhou', 'kaifeng', 'luoyang', 'pingdingshan', 'anyang', 'jiaozuo', 'sanmenxia', 'nanjing', 'wuxi', 'xuzhou', 'changzhou', 'suzhou', 'nantong', 'lianyungang', 'huaian', 'yancheng', 'yangzhou', 'zhenjiang', 'taizhou', 'suqian', 'hefei', 'wuhu', 'maanshan', 'huangshan', 'wuhan', 'jingzhou', 'yichang', 'enshi', 'hangzhou', 'ningbo', 'wenzhou', 'jiaxing', 'huzhou', 'shaoxing', 'jinhua', 'quzhou', 'zhoushan', 'taizhou', 'lishui', 'nanchang', 'jingdezhen', 'jiujiang', 'changsha', 'zhuzhou', 'xiangtan', 'yueyang', 'changde', 'zhangjiajie', 'fuzhou', 'xiamen', 'quanzhou', 'chengdou', 'panzhihua', 'luzhou', 'deyang', 'mianyang', 'yibin', 'nanchong', 'zigong', 'guiyang', 'zunyi', 'kunming', 'dali', 'qujing', 'yuxi', 'nanning', 'guilin', 'liuzhou', 'beihai', 'guangzhou', 'shenzhen', 'zhuhai', 'shantou', 'foshan', 'shaoguan', 'zhanjiang', 'maoming', 'zhaoqing', 'huizhou', 'meizhou', 'zhongshan', 'chaozhou', 'dongwan', 'wulumuqi', 'kelamayi', 'kuerle', 'haikou', 'sanya', 'huhehaote', 'baotou', 'chifeng', 'eerduosi', 'yinchuan', 'shizuishan', 'xining', 'lanzhou', 'jiayuguan', 'lasa', 'xianggang', 'aomen', 'taibei'] 

try_again_list = []


#smog_re = re.compile(r'^.*<table\sclass=\'api\'.*<tbody>.*"\s>([0-9]{1,3})</div>')
smog_re = re.compile(r'^.*<table\sclass=\'api\'.*<tr><td.*"\s>([0-9]{1,3})</div>')

# 美使馆PM2.5的查询URL: http://aqicn.org/city/beijing/cn/
# 构造列表中的URL
#city_pinyin_list = ['haerbin', 'beijing']
for i in city_pinyin_list:

    url =  'http://aqicn.org/city/' + i + '/cn/'
    #st = random.randint(6,16)
    #print "%d秒后获取下一城市" % st
    time.sleep(3)

    # 获取网页
    try:
        response = urllib2.urlopen(url)
        html = response.read()
    except urllib2.HTTPError, e:
        print city_list[city_pinyin_list.index(i)] + ' ' + '404 page not found'

    smog_match = smog_re.match(html)
    if smog_match:
        smog = smog_match.group(1)
        print str(city_list[city_pinyin_list.index(i)]) + '的PM2.5为: ' + smog
        # 写入数据库
        #cmd = 'UPDATE weather SET real_time_pm25=%s WHERE date="%s" AND city="%s"' % (smog, date, city_list[city_pinyin_list.index(i)])
        #print cmd
        #conn = MySQLdb.connect(host='localhost', port=3306, db='w_smog', user='user', passwd='123456')
        #cursor = conn.cursor()
        #cursor.execute(cmd)
        #conn.commit()
        #cursor.close()
        #conn.close()
    else:
        print "Some error"
        # Some err
        #cmd = 'UPDATE weather SET real_time_pm25=%s WHERE date="%s" AND city="%s"' % (0, date, city_list[city_pinyin_list.index(i)])
        #print cmd
        #conn = MySQLdb.connect(host='localhost', port=3306, db='w_smog', user='user', passwd='123456')
        #cursor = conn.cursor()
        #cursor.execute(cmd)
        #conn.commit()
        #cursor.close()
        #conn.close()








