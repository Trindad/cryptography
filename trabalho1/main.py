from sys import argv
from caesar_cipher import CaesarCipher
from transposition_cipher import TranspositionCipher
from vigenere_cipher import VigenereCipher

script,from_file,key = argv

#caesar = CaesarCipher()
# caesar.cipher(from_file,int(key))
#caesar.decipher(from_file,int(key))

# transposition = TranspositionCipher()
# transposition.cipher(from_file,int(key))

# transposition = TranspositionCipher()
# transposition.decipher(from_file,int(key))

# vigenere = VigenereCipher()
# vigenere.cipher(from_file,key)

vigenere = VigenereCipher()
vigenere.decipher(from_file,key)