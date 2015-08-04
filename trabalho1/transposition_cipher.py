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
				if it < key:
					while (it < key):
						matrix[line].append( ord(" ") )
						it += 1
				matrix = zip(*matrix)

				for i in range(0, len(matrix)):
					for j in range(0, len(matrix[0])):
						output.write( chr(matrix[i][j]) )
				f.close
		else:
			print "File not exists"

	def decipher(self,file,key):
		
		if	exists(file):
			output = open("transposition_decipher_"+file,'w+b')
			it = 0
			line = 0
			matrix = [[]]

			with open(file,'r+b') as f:
				key = len(f.read()) / key

				f.seek(0) 

				while 1:
					read_data = f.read(1)

					if not read_data:
						break
					
					if it == key:
						it = 0
						matrix.append([])
						line += 1

					matrix[line].append( read_data )
					it += 1
				if it < key:
					while (it < key):
						matrix[line].append( " " )
						it += 1
						
				for j in range(0, len(matrix[0])):
					for i in range(0, len(matrix)):
						output.write( matrix[i][j] )
				f.close
		else:
			print "File not exists"
