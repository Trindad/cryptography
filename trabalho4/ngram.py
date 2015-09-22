from sys import argv
import re
import random

class NGram:
	"""docstring for NGram"""
	def __init__(self):
		pass
	def unigrams(self,text):
		unigrams = {}

		for c in text:
			if c == " " or c == "\n":
				continue
			if c in unigrams:
				unigrams[c] += 1
			else:
				unigrams[c] = 1

		return unigrams

	def bigrams(self,text):
		bigrams = {}
		bigram = ""

		for c in text:
			if c == " " or c == "\n":
				continue
			if not bigram:
				bigram = c
				continue
			
			bigram += c

			if bigram in bigrams:
				bigrams[bigram] += 1
			else:
				bigrams[bigram] = 1
			bigram = c
		return bigrams
	
	def trigrams(self,text):
		trigrams = {}
		trigram = ""

		for c in text:
			if c == " " or c == "\n":
				continue
			if not trigram:
				trigram = c
				continue
			elif len(trigram) == 1:
				trigram += c
				continue

			trigram += c

			if trigram in trigrams:
				trigrams[trigram] += 1
			else:
				trigrams[trigram] = 1
			
			trigram = trigram[1:]
		return trigrams