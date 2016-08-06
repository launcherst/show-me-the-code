# -*-coding:utf8 -*-

import os,sys,string

def match_word(input):
	word = ''
	for i in range(len(input)):
		if input[i] not in string.ascii_letters: break
		word += input[i]
	return word

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
		for word in line.split():
			key = match_word(word).lower()
			if len(key) == 0: break
			if key in result: result[key] += 1
			else: result[key] = 1
	
	print(sorted(result.items()))