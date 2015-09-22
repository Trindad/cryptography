from sys import argv
import re
import random
from cipher import Cipher
from ngram import NGram
from break_cipher import BreakCipher

script,enc,text = argv

c = Cipher()
textEnc = c.cipher(enc)

dictionary =  c.processText(text)

b = BreakCipher()

b.breakCipher(textEnc,dictionary)

