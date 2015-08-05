from sys import argv
from caesar_cipher import CaesarCipher
from transposition_cipher import TranspositionCipher
from vigenere_cipher import VigenereCipher
from substitution_cipher import SubstitutionCipher

script,from_file,key,algorithm,option = argv


if algorithm == "c":

	caesar = CaesarCipher()

	if option == "c":
		caesar.cipher(from_file,int(key))
	elif option == "d":
		caesar.decipher(from_file,int(key))
	else:
		print "Option doesn't exist."
elif algorithm == "t":

	transposition = TranspositionCipher()

	if option == "c":
		transposition.cipher(from_file,int(key))
	elif option == "d":
		transposition.decipher(from_file,int(key))
	else:
		print "Option doesn't exist."
elif algorithm == "v":

	vigenere = VigenereCipher()

	if option == "c":
		vigenere.cipher(from_file,key)
	elif option == "d":
		vigenere.decipher(from_file,key)
	else:
		print "Option doesn't exist."
elif algorithm == "v":

	substitution = SubstitutionCipher()

	if option == "c":
		substitution.cipher(from_file,key)
	elif option == "d":
		substitution.decipher(from_file,key)
	else:
		print "Option doesn't exist."
else:
	print "Algorithm doesn't exist."
