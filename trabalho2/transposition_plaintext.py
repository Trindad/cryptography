from sys import argv, path
from os.path import exists
path.append("../trabalho1")
from transposition import Transposition

class TranspositionPlainText:
	"""docstring for TranspositionPlainText"""
	def __init__(self):
		pass

	def key(self,text,enc):

		output = open("transposition_key.txt",'w+b')
		key = 1

		while 1:
			transposition = Transposition()
			test = transposition.decipher(enc,key)

			if self.compare(text,test) == 1:
				break
			else:
				key = key+1
		print "key = "+str(key)

	def compare(self,text,test):
		
		with open(text,'r+b') as f:
			with open(test,'r+b') as f1:
				while 1:
					read_data = f.read(1)
					read_enc = f1.read(1)

					if not read_data:
						break

					if ord(read_data) != ord(read_enc):
						return 0
		return 1