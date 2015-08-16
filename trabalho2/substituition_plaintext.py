from sys import argv
from os.path import exists

class SubstituitionPlainText:
	"""docstring for SubstituitionPlainText"""
	def __init__(self, arg):
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
			f1.close
		f.close

		output = open("substituition_key.txt",'w+b')

		for key, value in dict.items():
			output.write( chr( key ) )
			output.write( chr( value ) )
			output.write( "\n" )

		output.close