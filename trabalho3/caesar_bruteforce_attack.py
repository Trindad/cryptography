from sys import argv,path
from os.path import exists
path.append("../trabalho1")
from caesar import Caesar

from nltk.corpus import words

class CaesarBruteForce(object):
	"""docstring for CaesarBruteForce"""
	def __init__(self):
		pass
	
	def breakOpen(self,enc):

		it = 1
		key = it
		words = 0

		while it < 255:
			
			caesar = Caesar()
			file = caesar.decipher(enc,it)

			n = self.compare(file)

			if n > words:
				key = it
				words = n

			it += 1

		print key
	
	def compare(self,file):
		
		word_list = []
		for a in words.words():
			word_list.append(str(a))

		text = []

		with open(file, "r+b") as f:

			while 1:
			 	read_data = f.read(1)

			 	if not read_data :
			 		break
			 	text.append(read_data)
		
		text = "".join(text)
		w = text.split(" ")

		occurencies = 0

		for s in w:
			if s in word_list:
				occurencies += 1

		return occurencies