from sys import argv
from caesar_bruteforce_attack import CaesarBruteForce
from transposition_bruteforce_attack import TranspositionBruteForce
from vigenere_bruteforce_attack import VigenereBruteForce

script,enc,algorithm = argv

if algorithm == "c":

	caesar = CaesarBruteForce()

	caesar.breakOpen(enc)

elif algorithm == "t":

	transposition = TranspositionBruteForce()

	transposition.breakOpen(enc)

elif algorithm == "v":

	vigenere = VigenereBruteForce()

	vigenere.breakOpen(enc)
else:
	print "Algorithm doesn't exist."