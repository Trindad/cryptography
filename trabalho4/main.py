from sys import argv
from substitution_break import SubstitutionBreak
from construct_dictionary import ConstructDictionary 

script,enc = argv

dic = ConstructDictionary();

# print dic.constructDigraphs("dictionary.txt");
# print dic.constructMonographs("dictionary.txt");
substitution = SubstitutionBreak();

substitution.breakOpen(enc);


