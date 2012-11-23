#!usr/bin/python
from copy import copy 
import sys

def find_words(letters):
	letters=list(letter_string.lower())

	words=[]
	found_words=[]
	
	with open("words.txt") as f:
		words = [line.strip() for line in f.readlines()]

	for word in words:
		word_as_list = list(word)
		for letter in letters:
			if letter in word_as_list:
				word_as_list.remove(letter)
			else:
				any_missing=True
		if len(word_as_list) == 0:
			found_words.append(word)
	found_words.sort(key=len)
	print "Top 5 words by length: "
	for word in found_words[-5:]:
		print word


if __name__=='__main__':
	letter_string=raw_input("Insert letters: \n")
	find_words(letter_string)

