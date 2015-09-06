from sys import argv
from substitution_break import SubstitutionBreak
from construct_dictionary import ConstructDictionary 

script,enc = argv

dic = ConstructDictionary();

print dic.construct("words.txt");

substitution = SubstitutionBreak();

substitution.beakOpen(enc);


