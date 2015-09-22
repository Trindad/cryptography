from sys import argv
import random
from math import log10

class HillClimbing:
	"""docstring for HillClimbing"""
	def __init__(self):
		pass

	def breakOpen(self,enc,keys,monographs,trigraphs):
		
		parent = keys

		test = self.decipher(enc,parent)
		currentResult = self.rateFitness(test,trigraphs.copy())

		count = 0
		currentTest = test

		# substituindo caracteres vetor de keys ate encontrar a melhor solucao
		while 1:
			#print count
			newParent = parent.copy()

			#swap de duas posicoes do parent
			k1 = random.choice(newParent.keys())
			k2 = self.newPosition(monographs,newParent,k1)

			print " "+newParent[k1]+" "+newParent[k2]
			temp = newParent[k1]
			newParent[k1] = newParent[k2]
			newParent[k2] = temp

			test = self.decipher(enc,parent)
			fitness = self.rateFitness(test,trigraphs.copy())

			# print str(fitness) + " "+str(currentResult)
			if fitness > currentResult:
				print " fitness "+str(fitness)
				currentTest = test
				currentResult = fitness
				parent = newParent
				count = 0
			else:
				if count >= 1000:
					break
				count += 1

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
		text = ""
		for x in enc:
			if x == " " or x == "\n":
				text += x
			else:
				text += key[x]
		return text

	def breakOpenBruteForce(self,enc,keys,monographs,trigraphs):
		
		parent = keys

		test = self.decipher(enc,parent)
		currentResult = self.rateFitness(test,trigraphs.copy())

		count = 0
		currentTest = test
		a1 = parent.keys()[:]
		a2 = parent.keys()[:]

		index1 = 0
		index2 = 0

		# substituindo caracteres vetor de keys ate encontrar a melhor solucao
		while index1 < len(a1):
			#print count
			newParent = parent.copy()

			#swap de duas posicoes do parent
			k1 = a1[index1]
			k2 = a2[index2]

			print " "+newParent[k1]+" "+newParent[k2]
			temp = newParent[k1]
			newParent[k1] = newParent[k2]
			newParent[k2] = temp

			test = self.decipher(enc,parent)
			fitness = self.rateFitness(test,trigraphs.copy())

			# print str(fitness) + " "+str(currentResult)
			if fitness > currentResult:
				print " fitness "+str(fitness)
				currentTest = test
				currentResult = fitness
				parent = newParent

			index2 += 1

			if index2 >= len(a2):
				index1 += 1
				index2 = 0

		print currentTest
