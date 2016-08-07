# -*-coding:utf8 -*-
# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import glob,string

def txt_list():
	return glob.glob("*.txt")

def match_word(line):
	words = []
	word = ''
	for letter in line:
		if letter in string.ascii_letters: word += letter
		else:
			words.append(word)
			word = ''
	return words

IGNOR_WORDS = {'the', 'a', 'of', 'in', 'on', 'is', 'are', 'was', 'were', 'above', 'and', 'or', 'to', 'from', 'as', 'for'}

if __name__ == '__main__':
	result = {}
	for filename in txt_list():
		with open(filename, 'r') as file:
			for line in file:
				for word in match_word(line):
					key = word.lower()
					if len(key) == 0 or key in IGNOR_WORDS: continue
					if key in result: result[key] += 1
					else: result[key] = 1
	print(sorted(result.items(),key=lambda d:d[1],reverse=True))