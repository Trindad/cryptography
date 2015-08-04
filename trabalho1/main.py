from sys import argv
from caesar_cipher import CaesarCipher
from transposition_cipher import TranspositionCipher

script,from_file,key = argv

#caesar = CaesarCipher()
# caesar.cipher(from_file,int(key))
#caesar.decipher(from_file,int(key))

# transposition = TranspositionCipher()
# transposition.cipher(from_file,int(key))

transposition = TranspositionCipher()
transposition.decipher(from_file,int(key))