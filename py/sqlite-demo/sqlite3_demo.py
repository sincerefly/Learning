# -*- coding: utf-8 -*-

import sqlite3
import json

db_name = 'shipping.db'
org_json_data = 'shipping_data.json'
table_rules = {'shipping_store': '''CREATE TABLE shipping_store (order_sn text primary key, logistics_name text, logistics_code text, robot_status integer, order_status text)'''}


def load_data(filename):

    with open(filename, 'r') as f:
        data = json.loads(f.read())

    return data


def init_database():

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()

    for table_name in table_rules.keys():
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        if cur.fetchone() == None:
            cur.execute(table_rules[table_name])


def save_data(data):

    tuple_list = []
    for i in data:
        tuple_list.append((i['order_id'], i['logistics_name'], i['logistics_code'], i['robot_status'], i['order_status']))

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    for item in tuple_list:
        order_sn = item[0]
        logistics_name = item[1]
        logistics_code = item[2]
        robot_status = item[3]
        order_status = item[4]
        cur.execute("INSERT OR REPLACE INTO shipping_store VALUES(?, ?, ?, ?, ?)", (order_sn, logistics_name, logistics_code, robot_status, order_status))
    conn.commit()
    conn.close()

def select_data():

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM shipping_store")
    data = cur.fetchall()
    for i in data:
        print i[0], i[1], i[2], i[3]
    conn.close()


if __name__ == '__main__':

    init_database()
    data = load_data(org_json_data)
    save_data(data)
    select_data()






