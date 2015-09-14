from sys import argv
import operator

class ConstructDictionary():

	def construct(self,file):

		str = ""
		dictionary = []

		with open(file, "r+b") as f:

			while 1:
			 	read_data = f.read(1)

			 	if not read_data :
			 		if not(str in dictionary) and len(str) >= 1:
			 			dictionary.append(str.strip())
			 		break
			 	if " " == read_data or "\t" == read_data or "\n" == read_data :
			 		if not(str in dictionary) and len(str) >= 1:
			 			dictionary.append(str.strip())
			 		str = ""
			 	else :
			 		str += read_data

		dic = "dictionary.txt"

		with open(dic, "w+b") as f:
			for i in dictionary:
				f.write(i+"\n")				

		return dic;

	def constructMonographs(self,file):
		
		dictionary = {}

		with open(file, "r+b") as f:
			while 1:
			 	read_data = f.read(1)

			 	if not read_data:
			 		break
			 	elif " " == read_data or "\r" == read_data or "\t" == read_data or "\n" == read_data:
			 		continue
			 	else:
			 		if read_data in dictionary :	
			 			dictionary[read_data] += 1
			 		else:
			 			dictionary[read_data] = 1

		monographs = "monographs.txt"
		
		with open(monographs, "w+b") as f:
			for one in sorted(dictionary,key=dictionary.get,reverse=True):
				monograph = one+" "+str(dictionary[one])+"\n"
				f.write(monograph)

	def constructDigraphs(self,file):
		
		dictionary = {}

		s = ""

		with open(file, "r+b") as f:
			while 1:
			 	read_data = f.read(1)

			 	if not read_data:
			 		break
			 	elif not s:
			 		s = read_data
			 	elif " " == read_data or "\r" == read_data or "\t" == read_data or "\n" == read_data:
			 		continue
			 	elif s:
			 		if s+read_data in dictionary :	
			 			dictionary[s+read_data] += 1
			 		else:
			 			dictionary[s+read_data] = 1
			 		s = read_data

		digraphs = "digraphs.txt"
		
		with open(digraphs, "w+b") as f:
			for pair in sorted(dictionary,key=dictionary.get,reverse=True):
				digraph = pair+" "+str(dictionary[pair])+"\n"
				f.write(digraph)

	def constructTrigraphs(self,file):
		
		dictionary = {}

		s = ""
		t = ""

		with open(file, "r+b") as f:
			while 1:
			 	read_data = f.read(1)

			 	if not read_data:
			 		break
			 	elif " " == read_data or "\r" == read_data or "\t" == read_data or "\n" == read_data:
			 		continue
			 	elif not s:
			 		s = read_data
			 	elif not t:
			 		t = s
			 		s = read_data
			 	else:
			 		if t+s+read_data in dictionary :	
			 			dictionary[t+s+read_data] += 1
			 		else:
			 			dictionary[t+s+read_data] = 1
			 		t = s
			 		s = read_data

		trigraphs = "trigraphs.txt"
		
		with open(trigraphs, "w+b") as f:
			for triplet in sorted(dictionary,key=dictionary.get,reverse=True):
				trigraph = triplet+" "+str(dictionary[triplet])+"\n"
				f.write(trigraph)
				