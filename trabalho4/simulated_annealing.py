from sys import argv
import random
from math import log10, exp

class SimulatedAnnealing:
	"""docstring for SimulatedAnnealing"""
	def __init__(self):
		pass

	def breakOpen(self,enc,keys,monographs,trigraphs):
		
		parent = keys

		test = self.decipher(enc,parent)
		currentResult = self.rateFitness(test,trigraphs.copy())

		currentTest = test
		t = 10.0

		while t > 0:
			count = 0
			# substituindo caracteres vetor de keys ate encontrar a melhor solucao
			while count < 10:
				newParent = parent.copy()

				#swap de duas posicoes do parent
				k1 = random.choice(newParent.keys())
				k2 = random.choice(newParent.keys())

				temp = newParent[k1]
				newParent[k1] = newParent[k2]
				newParent[k2] = temp

				test = self.decipher(enc,parent)
				fitness = self.rateFitness(test,trigraphs.copy())

				diff = fitness - currentResult
				
				if diff >= 0:
					
					currentTest = test
					currentResult = fitness
					parent = newParent
				elif t > 0:
					prob = exp(diff/t)
					if prob > random.random():
						# print " fitness "+str(fitness)
					 	currentTest = test
						currentResult = fitness
						parent = newParent 

				count += 1

			t -= 1

		print currentTest

	def newPosition(self,monographs,parent,k):
		k1 = parent[k]
		k2 = k1
		ant = float("inf")

		for x in monographs.keys():
			diff = abs(monographs[x]-monographs[k1])
			
			if  diff < ant and x != k1:
				k2 = x
				ant = diff
		for x in parent.keys():
			if parent[x] == k2:
				return x
		return k

	def rateFitness(self,text,trigraphs):
	
		score = 0
		n = 0

		for i in trigraphs:
			n += trigraphs[i]

		for x in trigraphs.keys():
			trigraphs[x] = log10(float(trigraphs[x])/n)
		floor = log10(0.01/n)

		for x in range(1,len(text)-3):
			triplet = text[x : x+3 ]

			if triplet in trigraphs:
				score += trigraphs[triplet]
			else:
				score += floor
		
		return score
	
	def decipher(self, enc, key):
		text = []
		for x in enc:
			if x == " " or x == "\n":
				text.append(x)
			else:
				text.append(key[x])
		return "".join(text)
