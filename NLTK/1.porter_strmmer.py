import nltk
from nltk.stem import PorterStemmer
word_stemmer = PorterStemmer()
q = word_stemmer.stem('writing')
print(q)
w = word_stemmer.stem('eating')
print(w)
