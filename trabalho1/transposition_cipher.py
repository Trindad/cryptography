from sys import argv
from os.path import exists

class TranspositionCipher(object):
	"""docstring for TranspositionCipher"""
	def __init__(self):
		pass

	def cipher(self,file,key):
		if	exists(file):
			output = open("transposition_cipher_"+file,'w+b')
			it = 0
			line = 0
			matrix = [[]]

			with open(file,'r+b') as f:
				while 1:
					read_data = f.read(1)

					if not read_data:
						break
					
					if it == key:
						it = 0
						matrix.append([])
						line += 1

					matrix[line].append( ord(read_data) )
					it += 1
				#preenche espaço da matriz caso a linha possua posições vazias
				if it < key:
					while (it < key):
						matrix[line].append( ord("\0") )
						it += 1
				matrix = zip(*matrix)#transposição da matriz
				print matrix
				f.close
		else:
			print "File not exists"

	def decipher(self,file,key):
		
		if	exists(file):
			output = open("transposition_cipher_"+file,'w+b')

			with open(file,'r+b') as f:
				while 1:
					read_data = f.read(1)
					
					if not read_data:
						break
					output.write( chr( ( ord(read_data) + key ) % 256 ) )
			f.close
		else:
			print "File not exists"
