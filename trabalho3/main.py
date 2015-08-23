from sys import argv
from caesar_bruteforce_attack import CaesarBruteForce
from transposition_bruteforce_attack import TranspositionBruteForce
from vigenere_bruteforce_attack import VigenereBruteForce

script,text,enc,algorithm = argv

if algorithm == "c":

	caesar = CaesarPlainText()

	caesar.key(text,enc)

elif algorithm == "t":

	transposition = TranspositionPlainText()

	transposition.key(text,enc)

elif algorithm == "v":

	vigenere = VigenerePlainText()

	vigenere.key(text,enc)
else:
	print "Algorithm doesn't exist."