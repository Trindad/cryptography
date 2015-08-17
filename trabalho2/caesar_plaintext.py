from sys import argv,path
from os.path import exists
path.append("../trabalho1")
from caesar import Caesar

class CaesarPlainText:
	"""docstring for CaesarPlainText"""
	def __init__(self):
		pass

	def key(self,text,enc):
		
		output = ""
		with open(text,'r+b') as f:
			with open(enc,'r+b') as f1:
				read_data = f.read(1)
				read_enc = f1.read(1)

			print "key = "+str( ( ord(read_enc) - ord(read_data)+256 ) % 256 )

			caesar = Caesar()
			test = caesar.decipher(enc,int( ( ord(read_enc) - ord(read_data)+256 ) % 256 ))

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