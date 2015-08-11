from sys import argv
from caesar import Caesar
from transposition import Transposition
from vigenere import Vigenere
from substitution import Substitution

script,from_file,key,algorithm,option = argv


if algorithm == "c":

	caesar = Caesar()

	if option == "c":
		caesar.cipher(from_file,int(key))
	elif option == "d":
		caesar.decipher(from_file,int(key))
	else:
		print "Option doesn't exist."
elif algorithm == "t":

	transposition = Transposition()

	if option == "c":
		transposition.cipher(from_file,int(key))
	elif option == "d":
		transposition.decipher(from_file,int(key))
	else:
		print "Option doesn't exist."
elif algorithm == "v":

	vigenere = Vigenere()

	if option == "c":
		vigenere.cipher(from_file,key)
	elif option == "d":
		vigenere.decipher(from_file,key)
	else:
		print "Option doesn't exist."
elif algorithm == "s":

	substitution = Substitution()

	if option == "c":
		substitution.cipher(from_file,key)
	elif option == "d":
		substitution.decipher(from_file,key)
	else:
		print "Option doesn't exist."
else:
	print "Algorithm doesn't exist."
