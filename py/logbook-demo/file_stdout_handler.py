# -*- coding: utf-8 -*-

from logbook import Logger, StreamHandler, FileHandler
import logbook
import sys

'''
记录日志到文件和STDOUT
'''

StreamHandler(sys.stdout, level='DEBUG').push_application()
FileHandler('app.log', bubble=True, level='INFO').push_application()

log = Logger('test')

def main():
    log.info('hello world')

if __name__ == '__main__':
    main()




