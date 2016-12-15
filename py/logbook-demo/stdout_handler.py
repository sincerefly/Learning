# -*- coding: utf-8 -*-

from logbook import Logger, StreamHandler
import logbook
import sys

handler = StreamHandler(sys.stdout)
log = Logger('test')

def main():
    log.info('something logging')

if __name__ == '__main__':
    with handler.applicationbound():
        main()




