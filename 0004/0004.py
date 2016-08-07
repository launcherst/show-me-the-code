# -*-coding:utf8 -*-

# 任一个英文的纯文本文件，统计其中的单词出现的个数

import os,sys,string

def match_word(line):
	words = []
	word = ''
	for letter in line:
		if letter in string.ascii_letters: word += letter
		else:
			words.append(word)
			word = ''
	return words

if __name__ == '__main__':
	infile_name = sys.argv[1]
	infile = open(infile_name)
	try:
		content = infile.read()
	finally:
		infile.close()
	
	infile = open(infile_name, 'r')
	
	result = {}
	
	for line in infile:
		for word in match_word(line):
			key = word.lower()
			if len(key) == 0: continue
			if key in result: result[key] += 1
			else: result[key] = 1
	
	print(sorted(result.items()))