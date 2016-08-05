# -*-coding:utf-8 -*-

# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。

# python 3.5暂时没有mysql的官方connector,可以用pymysql代替

import pyMySQL, string, random

KEY_LEN = 20
KEY_ALL = 200

class mysql_init(object):
	def __init__(self, coon):
		self.conn = None

	# connect to mysql
	def connect(self):
		self.conn = pyMySQL.connect(
			host = 'localhost',
			port = 3306,
			user = 'test'
			password = 'password',
			db = 'testDB',
			charset = 'utf8',
			)

	def cursor(self):
		return self.conn.cursor()

	def commit(self):
		return self.conn.commit()

	def close(self):
		return self.conn.close()

def process():
	dbconn.connect()
	conn = dbconn.cursor()
	DropTable(conn)
	CreateTable(conn)
	InsertDatas(conn)
	QueryData(conn)
	dbconn.close()

