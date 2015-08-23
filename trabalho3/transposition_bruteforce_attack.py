from sys import argv, path
from os.path import exists
path.append("../trabalho1")
from transposition import Transposition

from nltk.corpus import words

class TranspositionBruteForce(object):
	"""docstring for VigenereBruteForce"""
	def __init__(self):
		pass
	
		
	def breakOpen(self,file):
		word_list = words.words()