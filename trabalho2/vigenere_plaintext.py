from collections import Counter
from sys import argv
from os.path import exists

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
			self.principal_period(output)

	def check_repeat(self,s):
	    for i in range(1, len(s)):
	        substr = s[:i]
	        ratio = len(s)/len(substr)
	        if substr * ratio == s:
	            print 'Repeating on "%s"' % substr
	            return
	    print 'Non repeating'