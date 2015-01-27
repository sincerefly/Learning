#!/bin/env python
#encoding:utf-8
import os
import pymongo

DATA_DIR = 'data'

# 连接数据库
conn = pymongo.Connection('127.0.0.1', 27017)
#conn = pymongo.Connection('115.28.55.217', 27017)
db = conn.haha

# 读取subjects的info信息，获取subjects list
tmp = file('./data/info.txt', 'r').read()
sub_dict = eval(tmp)
sub_list = sub_dict.keys()

print sub_list
# 循环更新subjects表信息
index = 0
for nickname in sub_list:
    print nickname
    # 需要update的信息，保存在update_json中
    # 需要insert的信息，保存在init_json中
    index += 1
    title = sub_dict[nickname]['title']
    desc = sub_dict[nickname]['desc']
    update_json = {
            'nickname': nickname,
            'title': title,
            'desc': desc,
            'index': index
    }
    init_json = {
            'score': 0,
            'count': 0,
            'courses': [],
            'meta': {
                'createAt': '', # FIXME
                'updateAt': ''  # FIXME
            }
    }
    # 更新或插入数据

    db.subjects.update({"nickname": nickname}, {"$set":update_json, "$setOnInsert": init_json}, upsert=True)

# 循环更新courses表信息
#sub_list = ['sub-1']
for sub in sub_list:

    # 获取每个subject下的course列表
    tmp = file('./data/'+ sub +'/info.txt', 'r').read()
    crs_dict = eval(tmp)
    crs_list =  crs_dict.keys()

    # 循环遍历subject下的课程
    #crs_list = ['course-1']
    index = 0
    for crs in crs_list:
        index += 1
        title = crs_dict[crs]['title']
        desc = crs_dict[crs]['desc']
        type123 = crs_dict[crs]['type']
        pictureDir = './data/%s/%s' % (sub, crs)
        pictureCount = crs_dict[crs]['pictureCount']
        if type123 == 1:
            tmp = file(pictureDir + '/sample.json').read()
            sj = eval(tmp)
        else:
            sj = ""
        tmp = file(pictureDir + '/quiz.txt').read()
        quiz = eval(tmp)

        #print subject
        # 需要update的信息，保存在update_json中
        # 需要insert的信息，保存在init_json中
        update_json = {
                'nickname': crs,
                'index': index,
                'title': title,
                'desc': desc,
                'type': type123,
                'marketData': sj,
                'pictureDir': pictureDir[1:],
                'pictureCount': pictureCount
        }

        sub_id = db.subjects.find({'nickname':sub}, {'_id':1})[0]['_id']
        init_json = {
                'subject': sub_id,
                'count': 0,
                'score': 0,
                'exercises': []
        }

        db.courses.update({"nickname": crs, "subject": sub_id}, {"$set":update_json, "$setOnInsert": init_json}, True)
        # 返回的状态可判断执行为更新(true)还是插入(false)
        #status = db.runCommand('getlasterror')['updatedExisting']

        # 经过上面的 插入/更新 courses集合中有这个文档了，查询获得文档_id
        crs_id = db.courses.find({"nickname":crs, "subject": sub_id}, {'_id':1})[0]['_id']

        # 使用addToSet方法将_id插入到courses列表，addToSet可去重
        db.subjects.update({"_id":sub_id}, {"$addToSet": {"courses":crs_id}})

        if quiz.has_key('choices'):
            cho = quiz['choices']
        else:
            cho = []
        q = {
                'course': crs_id,
                'choices':cho
        }

        # 更新quizzes集合
        db.quizzes.update({'course':crs_id}, {'$set':{'choices':cho}}, upsert=True)

        quiz_list = db.quizzes.find({'course': crs_id}, {'_id':1})
        quiz_id_list = []
        for qid in quiz_list:
            quiz_id_list.append(qid['_id'])

        print quiz_id_list

        # 将quiz文档添加到对应的course中
        db.courses.update({'_id':crs_id}, {'$addToSet':{'exercises':{'$each':quiz_id_list}}})










