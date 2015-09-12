#!/usr/local/bin/python
#encoding:utf8

import MySQLdb
def get_tradeback_db(ip="localhost"):
    '''
    取行情数据库连接
    '''
    md_db = MySQLdb.connect(
			host=ip,
			port=3306,
			user='work',
			passwd='BJHR123',
			db="trade_bak",
			charset='utf8'
            )
    return md_db


def get_fcdb_db(ip="localhost"):
    '''
    取行情数据库连接
    '''
    md_db = MySQLdb.connect(
			host=ip,
			port=3306,
			user='root',
			passwd='BJHR123',
			db="fcdb",
			charset='utf8'
            )
    return md_db


def get_trade_db(ip="localhost"):
    '''
    取行情数据库连接
    '''
    md_db = MySQLdb.connect(
			host=ip,
			port=3306,
			user='root',
			passwd='BJHR123',
			db="trade",
			charset='utf8'
            )
    return md_db

def get_research_db(ip="localhost"):
    '''
    取行情数据库连接
    '''
    md_db = MySQLdb.connect(
			host=ip,
			port=3306,
			user='root',
			passwd='herong',
			db="research",
			charset='utf8'
            )
    return md_db

def get_centos_local_db():
	md_db = MySQLdb.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='herong',
			db="work",
			charset='utf8'
            )
	return md_db

def get_aliyun_db():
    '''
    取行情数据库连接
    '''
    md_db = MySQLdb.connect(
			host='42.121.120.9',
			port=3306,
			user='root',
			passwd='herong',
			db="work",
			charset='utf8'
            )
    return md_db


def get_shuchang_db():
    '''
    get shuchang db link
    '''
    db = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = 'root',
            passwd = '',
            db = 'bhstock',
            charset='utf8'
            )
    return db

def get_aliyun_md_db():
    '''
    get aliyun db link
    '''
    db = MySQLdb.connect(
            host = '42.121.120.9',
            port = 3306,
            user = 'root',
            passwd = 'herong',
            db = 'work',
            charset='utf8'
            )
    return db





def query_db_one(dbconn, sql, sqlargs):
	'''
	查询返回一个结果
	'''
	cursor = dbconn.cursor()
	cursor.execute(sql, sqlargs)
	result = cursor.fetchone()
	cursor.close()
	return result

def query_db_all(dbconn, sql, sqlargs):
	'''
	查询返回所有结果
	'''
	cursor = dbconn.cursor()
	cursor.execute(sql, sqlargs)
	result = cursor.fetchall()
	cursor.close()
	return result

def query_db_all_dict(dbconn, sql, sqlargs):
	'''
	查询返回所有结果，每个结果以关联数组形式存储
	'''
	cursor = MySQLdb.cursors.DictCursor(dbconn)
	cursor.execute(sql, sqlargs)
	result = cursor.fetchall()
	cursor.close()
	return result

def write_db(dbconn, sql, sqlargs):
	'''
	写数据库
	'''
	cursor = dbconn.cursor()
	cursor.execute(sql, sqlargs)
	cursor.close()

def write_innodb(dbconn, sql, sqlargs):
	'''
	写innodb引擎数据库
	'''
	cursor = dbconn.cursor()
	cursor.execute(sql, sqlargs)
	dbconn.commit()
	cursor.close()

def write_db_many(dbconn, sql, values):
	'''
	批量写数据库
	'''
	cursor = dbconn.cursor()
	cursor.executemany(sql, values)
	cursor.close()

def write_innodb_many(dbconn, sql, values):
	'''
	批量写innodb引擎数据库
	'''
	cursor = dbconn.cursor()
	cursor.executemany(sql, values)
	dbconn.commit()
	cursor.close()

if __name__ == "__main__":
	'''
	test
	'''
	db = get_md_db()
	sql = "select * from share_futures_tick limit 1"
	res = query_db_all_dict(db, sql, [])
	print res

