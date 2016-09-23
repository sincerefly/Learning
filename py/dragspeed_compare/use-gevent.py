#!/bin/env python3
# -*- coding: utf-8 -*-

import gevent
from gevent import monkey
import random
import requests
from bs4 import BeautifulSoup
monkey.patch_all()


urls = []
with open('urls.txt', 'r') as f:
    for url in f:
        urls.append(url.strip())


def parser_title(page):

    soup = BeautifulSoup(page, 'lxml')
    a = soup.find('div', 'report-title')
    return a.text.strip()

def print_title(url):

    page = requests.get(url).text
    title = parser_title(page)
    print('{}: {}'.format(url, title))


threads = [gevent.spawn(print_title, url) for url in urls]
gevent.joinall(threads)

