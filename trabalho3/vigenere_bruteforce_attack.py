from collections import Counter
from sys import argv,path
from os.path import exists
import re
path.append("../trabalho1")
from vigenere import Vigenere

from nltk.corpus import words

class VigenereBruteForce(object):
	"""docstring for VigenereBruteForce"""
	def __init__(self):
		pass
		
	def breakOpen(self,file):
		word_list = words.words()