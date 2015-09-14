from sys import argv,path
from os.path import exists
path.append("../trabalho1")
from substitution import Substitution
import random

class SubstitutionBreak:
	"""docstring for SubstitutionBreak"""
	def __init__(self):
		pass

	def breakOpen(self,enc):
		
		characters = []
		text = ""

		with open(enc, "r+b") as f:
			while 1:
			 	read_data = f.read(1)

			 	if not read_data:
			 		break
			 	else:
			 		text += read_data

		with open(enc, "r+b") as f:
			while 1:
			 	read_data = f.read(1)

			 	if not read_data:
			 		break
			 	else:
			 		if read_data not in characters :	
			 			characters.append(read_data)

		keys = {}
		possibilities = []

		for x in range(0,255):
			possibilities.append( chr(x) )

		for it in characters:
			random.shuffle(possibilities)
			keys[it] = possibilities.pop()

		parent = keys

		s = Substitution()

		test = s._decipher(text,parent)
		currentResult = self.rateFitness(test)

		count = 0

		# substituindo caracteres vetor de keys ate encontrar a melhor solucao
		while 1:
			print count
			newParent = parent.copy()

			#swap de duas posicoes do parent
			k1 = random.choice(newParent.keys())
			k2 = random.choice(newParent.keys())

			temp = newParent[k1]
			newParent[k1] = newParent[k2]
			newParent[k2] = temp

			test = s._decipher(text,parent)
			fitness = self.rateFitness(test)

			if fitness > currentResult:
				currentResult = fitness
				parent = newParent
				count = 0
			else:
				if count >= 1000:
					break
				count += 1

	def rateFitness(self,text):

		return 0


		
