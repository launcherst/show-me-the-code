# -*- coding:utf-8 -*-

# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券）

import random, string

'''
主键+随机码的方式.

这种方法优点：使用简单，不用直接去查询数据库，可以根据邀请码直接得到主键id,
然后根据id去数据库查询(速度很快)，再比较查询出来的邀请码和用户提交的邀请码是否一致。

生成:id(数据库primary key )->16进制 + "L(标识符)" +随机码
获取id:获取16进制的id再转回10进制
'''

def activation_code(id, length=10):
	prefix = hex(int(id))[2:] + 'L'
	length = length - len(prefix)
	chars = string.ascii_letters + string.digits
	return prefix + ''.join([random.choice(chars) for i in range(length)])

def get_id(code):
	return str(int(code.upper(), 16))

if __name__ == '__main__':
	for i in range(10, 500, 35):
		code = activation_code(i)
		id_hex = code.split('L')[0]
		id = get_id(id_hex)