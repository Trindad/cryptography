from collections import Counter
from sys import argv,path
from os.path import exists
import re
path.append("../trabalho1")
import itertools
from vigenere import Vigenere

from nltk.corpus import brown

class VigenereBruteForce(object):
	"""docstring for VigenereBruteForce"""
	def __init__(self):
		pass
		
	def breakOpenDic(self,enc):

		key = ""
		words = 0

		word_list = []

		for a in words.words():
			word_list.append(str(a))
		
		for a in word_list:	
			vigenere = Vigenere()
			file = vigenere.decipher(enc,a)

			n = self.compare(file)

			if n > words:
				key = a
				words = n
		print key
	
	def breakOpen(self,enc):

		lower_a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		upper_a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		
		all = []
		all = lower_a + upper_a + num

		words = 0
		key = ""

		for r in range(1, 5):
		    for s in itertools.product(all, repeat = r):
				vigenere = Vigenere()
				file = vigenere.decipher(enc,''.join(s))

				n = self.compare(file)

				if n > words:
					key = ''.join(s)
					words = n
		print key
	
	def compare(self,file):
		
		word_list = []
		for a in brown.words(fileids=['cc17']):
			word_list.append(str(a))

		word_list = set(word_list)

		text = []

		with open(file, "r+b") as f:

			while 1:
			 	read_data = f.read(1)

			 	if not read_data :
			 		break
			 	text.append(read_data)
		
		text = "".join(text)
		w = set( text.split() )

		occurencies = len(word_list & w)

		return occurencies