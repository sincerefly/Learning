#!/bin/env python
#encoding:utf-8
import os
import pymongo

DATA_DIR = 'data'

# connect db
conn = pymongo.Connection('127.0.0.1', 27017)
#conn = pymongo.Connection('115.28.55.217', 27017)
db = conn.haha

db.subjects.remove()
db.courses.remove()
db.quizzes.remove()

# get subs
tmp = file('./data/info.txt', 'r').read()
sub_dict = eval(tmp)
sub_list = sub_dict.keys()
#print sub_dict.values()[1]['desc']

index = 0
for i in sub_list:
    index += 1
    title = sub_dict[i]['title']
    desc = sub_dict[i]['desc']
    json = {
            'nickname': i,
            'title': title,
            'desc': desc,
            'index': index,
            'score': 0,
            'count': 0,
            'courses': [],
            'meta': {
                'createAt': '',
                'updateAt': ''
            }
    }
    db.subjects.insert(json)




#sub_list = ['sub-1']
for sub in sub_list:
    tmp = file('./data/'+ sub +'/info.txt', 'r').read()
    crs_dict = eval(tmp)
    crs_list =  crs_dict.keys()
    print crs_list

    index = 0
    #crs_list = ['course-1']
    for crs in crs_list:
        index += 1
        title = crs_dict[crs]['title']
        desc = crs_dict[crs]['desc']
        type123 = crs_dict[crs]['type']
        print "==================="
        print sub
        print crs
        print  crs_dict[crs]['type']
        print type(type123)
        print "==================="
        print type123
        pictureDir = './data/%s/%s' % (sub, crs)
        pictureCount = crs_dict[crs]['pictureCount']
        if type123 == 1:
            tmp = file(pictureDir + '/sample.json').read()
            sj = eval(tmp)
        else:
            sj = ""
        tmp = file(pictureDir + '/quiz.txt').read()
        quiz = eval(tmp)
        subject = db.subjects.find({'nickname':sub}, {'_id':1})[0]['_id']

        #print subject
        json = {
                'nickname': crs,
                'subject': subject,
                'index': index,
                'title': title,
                'desc': desc,
                'type': type123,
                'marketData': sj,
                'pictureDir': pictureDir[1:],
                'pictureCount': pictureCount,
                'count': 0,
                'score': 0,
                'exercises': [],
        }
        #print json
        db.courses.insert(json)
        courseid = db.courses.find({'nickname':crs, 'subject':subject}, {'_id':1})[0]['_id']

        print courseid

        if quiz.has_key('choices'):
            cho = quiz['choices']
        else:
            cho = []
        q = {
                'course':courseid,
                'choices':cho
        }
        print q
        db.quizzes.insert(q)

        quiz_list = db.quizzes.find({'course':courseid}, {'_id':1})
        quiz_id_list = []
        for qid in quiz_list:
            print "123"
            quiz_id_list.append(qid['_id'])
        print "----------"
        print quiz_id_list

        db.courses.update({"_id":courseid}, {"$addToSet":{"exercises":{"$each":quiz_id_list}}})

    course_id_list = []
    subject = db.subjects.find({'nickname':sub}, {'_id':1})[0]['_id']
    print "qqq"
    print subject
    course_list = db.courses.find({'subject':subject}, {'_id':1})
    for cid in course_list:
        print cid['_id'], "111=========="
        course_id_list.append(cid['_id'])

    print course_id_list

    db.subjects.update({"nickname":sub},{"$set":{"courses":course_id_list}})







