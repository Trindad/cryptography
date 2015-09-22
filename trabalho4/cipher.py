from sys import argv
import re
import random

class Cipher:
	"""docstring for Cipher"""
	def __init__(self):
		pass
	def cipher(self,file):
		
		possibilities = ['a','b','c','d','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

		processedText = self.processText(file)

		keys = {}

		for x in processedText:
			if x not in keys :
				if x == " " or x == "\n":
					keys[x] = x
				else:
					random.shuffle(possibilities)
					keys[x] = possibilities.pop()

		text = ""

		for x in processedText:
			text += keys[x]

		return text
	
	def processText(self,file):
		text = ""

		with open(file) as f:
			while 1:
				c = f.read(1)
				if not c:
					break
				text += c

		return re.sub(r'[^a-zA-Z ]+', ' ', text)