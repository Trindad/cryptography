from sys import argv
import re
import random
from cipher import Cipher
from ngram import NGram
from hill_climbing import HillClimbing
from simulated_annealing import SimulatedAnnealing

class BreakCipher:
	"""docstring for BreakCipher"""
	def __init__(self):
		pass

	def breakCipher(self,enc,dictionary):
		
		ngrams = NGram()

		uniEnc = ngrams.unigrams(enc)

		biEnc = ngrams.bigrams(enc)

		triEnc = ngrams.trigrams(enc)


		uniDictionary = ngrams.unigrams(dictionary)

		biDictionary = ngrams.bigrams(dictionary)

		triDictionary = ngrams.trigrams(dictionary)

		sort_tg_enc = sorted(uniEnc,key=uniEnc.get,reverse=True)
		sort_tg_dic = sorted(uniDictionary,key=uniDictionary.get,reverse=True)

		key = {}

		for index,x in enumerate(sort_tg_enc):
			key[x] = sort_tg_dic[index]

		# text = ""
		# for x in enc:
		# 	if x == " " or x == "\n":
		# 		text += x
		# 	else:
		# 		text += key[x]

		h = SimulatedAnnealing()

		h.breakOpen(enc,key,uniDictionary,triDictionary)
		