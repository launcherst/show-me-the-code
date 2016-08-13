# -*-coding:utf8 -*-

# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中
# 先使用sqlite3代替MySQL

import os,sys,sqlite3,string,random

KEY_LEN = 10
KEY_COUNT = 20
KEY_DICT = string.ascii_letters+string.digits

def key_gen(count=KEY_COUNT, length=KEY_LEN):
	result = []
	while len(result) < count:
		key = ''.join([random.choice(KEY_DICT) for i in range(length)])
		if key not in result: result.append(key)			
	return result
	
if __name__ == '__main__':
	#initialize the db
	db_file = os.path.join(os.path.dirname(__file__),'test.db')
	if os.path.isfile(db_file):
		os.remove(db_file)

	conn = sqlite3.connect(db_file)
	cur = conn.cursor()
	cur.execute(
		'create table key_pool (id INTEGER PRIMARY KEY,key varchar(255) NOT NULL UNIQUE)'
	)
		
	key_pool = key_gen()

	for i in range(KEY_COUNT):
		cur.execute("INSERT INTO key_pool (key) VALUES ('%s');" %key_pool.pop())

	cur.close()
	conn.commit()
	conn.close()