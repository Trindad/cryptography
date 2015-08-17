from collections import Counter
from sys import argv,path
from os.path import exists
import re
path.append("../trabalho1")
from vigenere import Vigenere

class VigenerePlainText:
	"""docstring for VigenerePlainText"""
	def __init__(self):
		pass

	def key(self,text,enc):
		
		output = ""
		with open(text,'r+b') as f:
			with open(enc,'r+b') as f1:
				while 1:
					read_data = f.read(1)
					read_enc = f1.read(1)
					
					if not read_data:
						break
					output += chr( (ord(read_enc) - ord(read_data)+256 ) % 256 )
		r = re.compile(r"(.+?)\1+")
		print r.findall(output)

		vigenere = Vigenere()
		test = vigenere.decipher(enc,r.findall(output)[0])

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