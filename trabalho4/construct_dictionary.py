from sys import argv

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