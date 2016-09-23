#!/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import bs4
import tqdm


urls = []
with open('urls.txt', 'r') as f:
    for url in f:
        urls.append(url.strip())


@asyncio.coroutine
def get(*args, **kwargs):
    response = yield from aiohttp.request('GET', *args, **kwargs)
    return (yield from response.text())


@asyncio.coroutine
def wait_with_progress(coros):
    for f in tqdm.tqdm(asyncio.as_completed(coros), total=len(coros)):
        yield from f


def parser_title(page):
    soup = bs4.BeautifulSoup(page, 'lxml')
    a = soup.find('div', 'report-title')
    return a.text.strip()


@asyncio.coroutine
def print_title(url):
    with (yield from sem):
        page = yield from get(url, compress=True)
    title = parser_title(page)
    print('{}: {}'.format(url, title))


sem = asyncio.Semaphore(5)
loop = asyncio.get_event_loop()
f = asyncio.wait([print_title(url) for url in urls])
#f = wait_with_progress([print_title(url) for url in urls])
loop.run_until_complete(f)




