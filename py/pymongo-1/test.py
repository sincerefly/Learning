#!/bin/env python
#encoding:utf-8
import os
import pymongo

DATA_DIR = 'data'

# 连接数据库
conn = pymongo.Connection('127.0.0.1', 27017)
#conn = pymongo.Connection('115.28.55.217', 27017)
db = conn.haha


db.users.remove()

# Insert & Save
db.users.insert({'name': 'user1', 'age': 16, 'index': 1})
db.users.insert({'name': 'user2', 'age': 17, 'index': 2})
db.users.insert({'name': 'user3', 'age': 18, 'index': 3})
db.users.save({'name': 'user4', 'age': 19, 'index': 4})

# Update
db.users.update({'name':'user1'}, {'$set': {'age': 20}})
json = {
        'age':20
}
db.users.update({'name':'user2'}, {'$set': json})

# Upsert
db.users.update({'name':'user5'}, {'$set': {'age': 22}, '$setOnInsert': {'index':5}}, upsert=True)

json = {
        'age':36
}
name = 'user5'
db.users.update({'name':name}, {'$set': json, '$setOnInsert': {'index':5}}, upsert=True)

# ----------------------------------------------------
update_json = {
        'nickname': 'hahahaha',
        'title': 'biaoti',
        'desc': 'miaoshu',
        'index': 36
}

init_json = {
        'score': 0,
        'count': 0,
        'courses': [],
        'meta':{
            'createAt':'',
            'updateAt':''
        }
}
nickname = 'user6'
db.users.update({'nickname': nickname}, {'$set':update_json, '$setOnInsert': init_json}, upsert=True)



