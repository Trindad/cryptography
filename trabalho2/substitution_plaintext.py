from sys import argv,path
from os.path import exists
path.append("../trabalho1")
from substitution import Substitution

class SubstitutionPlainText:
	"""docstring for SubstituitionPlainText"""
	def __init__(self):
		pass

	def key(self,text,enc):
		
		dict = {}

		with open(text,'r+b') as f:
			with open(enc,'r+b') as f1:
				while 1:
					read_data = f.read(1)
					read_enc = f1.read(1)
					
					if not read_data:
						break
					dict[ ord( read_data ) ] =  ord( read_enc ) 

		output = open("substituition_key.txt",'w+b')

		for key, value in dict.items():
			output.write( chr( key ) )
			output.write( chr( value ) )
			output.write( "\n" )
		output.flush()
		output.close()

		substitution = Substitution()
		test = substitution.decipher(enc,"substituition_key.txt")

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