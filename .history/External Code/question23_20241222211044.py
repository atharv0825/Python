# 23. program for applying the stemming operation using NLTK 
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["running","working","found","easily","writing"]

print("original word ")
for word in words: