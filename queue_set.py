#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import config
from db import SQLighter
import sys
chatid = sys.argv[1]
arg3 = str(sys.argv[2]).split(config.delmiter,2)
zabbixid = arg3[0]
triggerstatus = arg3[1]
text = arg3[2]
db = SQLighter(os.path.abspath(os.path.dirname(__file__))+'/db/msgdb')
count=db.countzabbix(zabbixid,chatid)
if count == 0 and triggerstatus == config.triggerbad:
    db.insert(zabbixid,chatid,text)

elif count != 0 and triggerstatus == config.triggergood:
    for row in db.select_all():
        if str(row[5]) == chatid and zabbixid == str(row[1]):
            db.mark_for_del(row[0])

db.close()







#


#    msg = bot.send_message(message.chat.id,	message.text)
# msg = bot.send_message(190070176,'test')
# msg = bot.delete_message(190070176,231)

#    bot.delete_message(message.chat.id,msg.message_id)

#if	__name__	==	'__main__':
#	bot.polling(none_stop=True)
