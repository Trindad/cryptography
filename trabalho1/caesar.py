from sys import argv
from os.path import exists

class Caesar:
	"""docstring for CaesarCipher"""
	def __init__(self):
		pass

	def cipher(self,file,key):
		
		if	exists(file):
			output = open("caesar_cipher.txt",'w+b')
			with open(file,'r+b') as f:
				while 1:
					read_data = f.read(1)
					
					if not read_data:
						break
					output.write( chr( ( ord(read_data) + key ) % 256 ) )
			f.close
		else:
			print "File not exists"

	def decipher(self,file,key):
		if	exists(file):
			output = open("caesar_decipher.txt",'w+b')
			with open(file,'r+b') as f:
				while 1:
					read_data = f.read(1)
					
					if not read_data:
						break
					output.write( chr( ( ord(read_data) - key ) % 256 ) )
			f.close
		else:
			print "File not exists"

		
		