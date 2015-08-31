from sys import argv, path
from os.path import exists
path.append("../trabalho1")
from transposition import Transposition

from nltk.corpus import brown

class TranspositionBruteForce(object):
	"""docstring for VigenereBruteForce"""
	def __init__(self):
		pass
	
	def breakOpen(self,enc):

		it = 1
		key = it
		words = 0
		limit = 0
		s = ""

		with open(enc, "r+b") as f:
			while 1:
				data = f.read(1)
				if not data :
			 		break
			 	s += data
		limit = len(s)

		# print limit

		while it <= limit:
			
			transposition = Transposition()
			file = transposition.decipher(enc,it)

			n = self.compare(file)

			# print str(it) + " "+ str(n)
			if n > words:
				key = it
				words = n
			it += 1

		print key

	def compare(self,file):
		
		word_list = []
		for a in brown.words(fileids=['cc17','ca16']):
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