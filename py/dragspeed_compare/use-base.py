#!/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
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


for url in urls:
    print_title(url)
