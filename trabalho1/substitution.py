from sys import argv
from os.path import exists

class Substitution:
	"""docstring for SubstitutionCipher"""
	def __init__(self):
		pass

	def cipher(self,file,keyfile):

		if exists(keyfile):		
			dict = {}
			with open(keyfile,'r+b') as auxiliar:
				while 1:
					key = auxiliar.read(1)
					
					if not key:
						break

					value = auxiliar.read(1)

					if not value:
						break
					dict[ ord( key ) ] =  ord( value ) 

					auxiliar.read(1)		
			auxiliar.close
		else:
			print "File not exists"
		if	exists(file):
			output = open("substituition_cipher.txt",'w+b')
			with open(file,'r+b') as f:
				while 1:
					read_data = f.read(1)
					
					if not read_data:
						break
					output.write( chr( dict[ ord(read_data) ] ) )
			f.close
		else:
			print "File not exists"

	def decipher(self,file,keyfile):
		if exists(keyfile):		
			dict = {}
			with open(keyfile,'r+b') as auxiliar:
				while 1:
					key = auxiliar.read(1)
					
					if not key:
						break

					value = auxiliar.read(1)

					if not value:
						break
					dict[ ord( value ) ] = ord( key )

					auxiliar.read(1)		
			auxiliar.close
		else:
			print "File not exists"
		if	exists(file):
			output = open("substituition_decipher.txt",'w+b')
			with open(file,'r+b') as f:
				while 1:
					read_data = f.read(1)
					
					if not read_data:
						break
					output.write( chr( dict[ ord(read_data) ] ) )
			output.close
		else:
			print "File not exists"

		return "substituition_decipher.txt"

	def _decipher(self,text,keys):
		
		output = []	

		for c in text:
			output.append(keys[c])
		return "".join(output)