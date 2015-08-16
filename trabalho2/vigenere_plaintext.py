from collections import Counter
from sys import argv
from os.path import exists
import re

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