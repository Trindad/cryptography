from sys import argv
from caesar_plaintext import CaesarPlainText
from transposition_plaintext import TranspositionPlainText
from vigenere_plaintext import VigenerePlainText
from substitution_plaintext import SubstitutionPlainText

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

elif algorithm == "s":

	substitution = SubstitutionPlainText()

	substitution.key(text,enc)
else:
	print "Algorithm doesn't exist."