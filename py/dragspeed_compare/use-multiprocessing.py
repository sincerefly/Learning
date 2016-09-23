#!/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
from bs4 import BeautifulSoup
import os, time
import requests


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


p = Pool(processes=4)
for url in urls:
    p.apply_async(print_title, args=(url,))
p.close()
p.join()
