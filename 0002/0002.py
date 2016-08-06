# -*-coding:utf8 -*-

# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
# 先使用sqlite3代替MySQL

import os,sqlite3,string,random

db_file = os.path.join(os.path.dirname(__file__),'test.db')
if os.path.isfile(db_file):
	os.remove(db_file)

KEY_POOL = string.ascii_letters+string.digits
def activation_code(length = 20):
	return ''.join([random.choice(KEY_POOL) for i in range(length)])

if __name__ == '__main__':
	#initialize the db
	conn = sqlite3.connect(db_file)
	cur = conn.cursor()
	cur.execute(
		'create table SN (id INTEGER PRIMARY KEY,sn varchar(255) NOT NULL UNIQUE)'
		)
	cur.execute('create index sn_index on SN(sn)')

	sn_pool = set()
	while len(sn_pool)<20:
		sn_pool.add(activation_code())

	for i in range(20):
		cur.execute("INSERT INTO SN (sn) VALUES ('%s');" %sn_pool.pop())

	cur.close()
	conn.commit()
	conn.close()