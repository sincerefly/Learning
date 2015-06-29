#!/bin/env python
#encoding:utf-8
import requests

#payload = {'key1': 'value1', 'key2[]': ['value2', 'value3']}
#r = requests.get("https://api.github.com/events", params=payload)

proxies = {
    'http': 'http://127.0.0.1:1080',
    'https': 'http://127.0.0.1:1080',
}

#r = requests.get("https://www.google.com/ncr", proxies=proxies)
#r = requests.get("https://www.baidu.com")
#r = requests.get("http://meez.in/a/18.html")
r = requests.get("https://api.github.com/events")
j = r.json()
print j[0]['id']
print r.status_code == requests.codes.ok
print r.headers['Content-Type']
print r.headers.get('content-type')

r = requests.head('http://www.github.com', allow_redirects=True)
print r.url
print r.status_code
print r.history

try:
    r = requests.get('http://github.com', timeout=0.001)
#except requests.exceptions.ConnectTimeout:
except requests.exceptions.Timeout:
    print "time out"







