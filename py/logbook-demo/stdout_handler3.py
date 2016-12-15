# -*- coding: utf-8 -*-

from logbook import Logger, StreamHandler
import logbook
import sys
import threading

'''
使用threadbound()只针对当前进程
'''

handler = StreamHandler(sys.stdout)
log = Logger('test')

def worker():
    log.info('something logging')

if __name__ == '__main__':
    #with handler.applicationbound():
    with handler.threadbound():
        log.info('main thread')
        t = threading.Thread(target=worker)
        t.start()




