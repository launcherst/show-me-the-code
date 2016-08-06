# -*-coding:utf8 -*-

# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
# iPhone5的分辨率1136x640

import os,sys,PIL

from PIL import Image,ImageDraw

extension_list = {'.jpg', '.png', '.bmp', '.jpeg', }

def get_new_size(w,h):
	w = int(w / max(w/1136, h/640, 1))
	h = int(h / max(w/1136, h/640, 1))
	return (w,h)

if __name__ == '__main__':
	path = sys.argv[1]
	#实验证明python在处理时会自动将尾部的/去掉
	#严格意义上需要校验参数的有效性
	'''
	try:
		os.path.isdir(path)
		os.path.exists(path)
	'''
	file_list = os.listdir(path)
	for filename in file_list:
		ext = os.path.splitext(filename)[1]
		if ext in extension_list:
			im = Image.open(os.path.join(path,filename))
			w,h = im.size
			im_resized = im.resize(get_new_size(w,h), Image.ANTIALIAS)
			new_filename = os.path.splitext(filename)[0] + '-副本' + ext
			im_resized.save(os.path.join(path,new_filename))