# -*-coding:utf8 -*-

# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来

import glob

def analyze_program(file_name):
	line_count = 0
	comment_flag = False
	space_line_count = 0
	comment_line_count = 0
	with open(filename, 'rb') as file:
		for line in file:
			line_count += 1
			if not line.strip(): space_line_count += 1
			elif line.startswith(b'#'): comment_line_count += 1
			elif line.startswith(b"'''") or line.startswith(b'"""'):
				comment_flag = not comment_flag
				if comment_flag: comment_line_count += 1
		print('file %s has %d lines:'%(filename,line_count))
		print('%d space lines'%space_line_count)
		print('%d comment_lines\n'%comment_line_count)

if __name__ == '__main__':
	for filename in glob.glob("*.py"):
		analyze_program(filename)