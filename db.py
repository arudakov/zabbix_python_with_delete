# -*- coding: utf-8 -*-
import sqlite3

class	SQLighter:
    def	__init__(self,	database):
		self.connection	=	sqlite3.connect(database)
		self.cursor	=	self.connection.cursor()
    def countzabbix(self,zabbixid,chatid):
        with self.connection:
            return self.cursor.execute('SELECT COUNT(id) from messages where zabbixid=? and chatid=? and deleted=0',(zabbixid,chatid)).fetchone()[0]
    def select_all(self):
        with self.connection:
            return self.cursor.execute('SELECT * from messages').fetchall()
    def insert(self,zabbixid,chatid,text):
        with self.connection:
            self.cursor.execute('insert into messages(zabbixid,chatid,text) values(?,?,?)',(zabbixid,chatid,text.decode ('utf8')))

    def delete(self, id):
        with self.connection:
            self.cursor.execute('DELETE from messages where id=?', (id,))

    def mark_for_del(self, id):
        with self.connection:
            self.cursor.execute('UPDATE messages set deleted=1 where id=?', (id,))
    def set_sended(self, id,msg_id):
        with self.connection:
            self.cursor.execute('UPDATE messages set messageid=? where id=?', (msg_id,id))

    def close(self):
        self.connection.close()


