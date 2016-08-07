# -*-coding:utf-8-*-

#将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。

from __future__ import print_function

import os,sys
from PIL import Image,ImageDraw,ImageFont

infile, pstext = sys.argv[1:]
f, e = os.path.splitext(infile)
outfile = f + '-副本.jpg'
try:
	im = Image.open(infile)
	w, h = im.size
	ps = ImageDraw.Draw(im)
	myfont = ImageFont.truetype('c:/fztmpfont.ttf', size = int(w/4))
	fillcolor = '#0000FF'
	ps.text((w-w/8, 0), pstext, font = myfont, fill = fillcolor)
	im.save(outfile, 'jpeg')
except IOError:
	print ('cannot ps %s file', infile)