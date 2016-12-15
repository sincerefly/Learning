# -*- coding: utf-8 -*-

from logbook import Logger, StreamHandler, Processor
import logbook
import sys

logbook.set_datetime_format('local')
handler = StreamHandler(sys.stdout)
handler.format_string = '[{record.time:%Y-%m-%d %H:%M:%S}] IP:{record.extra[ip]} {record.level_name}: {record.channel}: {record.message}'
handler.formatter

log = Logger('test')

def inject_ip(record):
    record.extra['ip'] = '127.0.0.1'

with handler.applicationbound():
    with Processor(inject_ip).applicationbound():
        log.error('something error')







