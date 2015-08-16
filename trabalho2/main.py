from sys import argv
# from caesar_plaintext import CaesarPlainText
# from transposition_plaintext import TranspositionPlainText
from vigenere_plaintext import VigenerePlainText
# from substitution_plaintext import SubstitutionPlainText

script,text,enc = argv

vigenere = VigenerePlainText()

vigenere.key(text,enc)


# caesar = CaesarPlainText()

# caesar.key(text,enc)

# transposition = TranspositionPlainText()

# transposition.key(text,enc)