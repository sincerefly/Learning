# -*- coding: utf-8 -*-

from logbook import Logger, MailHandler
import logbook
import sys

sender = 'Logger<sender@qq.com>'
recipients = ['123456@qq.com']
email_user = 'sender@qq.com'
email_pass = 'adpamkzzsppgnasgac'

mail_handler = MailHandler(sender, recipients,
        server_addr='smtp.qq.com',
        starttls=False,
        secure = True,
        credentials=(email_user, email_pass),
        format_string=u'''\
            Subject: {record.level_name} on My Application

            Message type: {record.level_name}
            Location: {record.filename}:{record.lineno}
            Module: {record.module}
            Function: {record.func_name}
            Time: {record.time:%Y-%m-%d %H:%M:%S}
            Remote IP: {record.extra[ip]}
            Request: {record.extra[url]} [{record.extra[method]}]
            Message: {record.message}
            ''',
        bubble=True)

log = Logger('test')

def main():
    log.info('something logging')

if __name__ == '__main__':
    with mail_handler.threadbound():
        main()




