#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from config import token
import telebot
bot = telebot.TeleBot(token)
from db import SQLighter
db = SQLighter(os.path.abspath(os.path.dirname(__file__))+'/db/msgdb')
for row in db.select_all():
   if row[3] is None and row[4] == 0:
      try:
         msg=bot.send_message(row[5],row[2])
         if msg.message_id is not None:
            db.set_sended(row[0],msg.message_id)
      except:
         exit(1)
   elif row[3] is None and row[4] == 1:
      db.delete(row[0])
   elif row[3] is not None and row[4] == 1:
      try:
         msgdeleted=bot.delete_message(row[5],row[3])
         if msgdeleted == True:
            db.delete(row[0])
      except:
         exit(1)

db.close()


