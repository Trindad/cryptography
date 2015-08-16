from sys import argv
from os.path import exists

class CaesarPlainText:
	"""docstring for CaesarPlainText"""
	def __init__(self):
		pass

	def key(self,text,enc):
		
		output = open("caesar_key.txt",'w+b')

		with open(text,'r+b') as f:
			with open(enc,'r+b') as f1:
				read_data = f.read(1)
				read_enc = f1.read(1)

				print "key = "+str( (ord(read_enc) - ord(read_data)+256 ) % 256 ) )
		output.close