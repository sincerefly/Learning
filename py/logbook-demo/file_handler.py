# -*- coding: utf-8 -*-

from logbook import Logger, FileHandler
import logbook
import sys

handler = FileHandler('app.log')
handler.push_application()
log = Logger('test')

def main():
    log.info('something logging')

if __name__ == '__main__':
    main()




