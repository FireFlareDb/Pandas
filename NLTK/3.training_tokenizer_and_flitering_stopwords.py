import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext, stopwords

#nltk.download()
text = webtext.raw('/home/secos/Desktop/NLTK/training_tokenizer.txt')
sent_tokenizer = PunktSentenceTokenizer(text)
sents_1 = sent_tokenizer.tokenize(text)
print(sents_1[0])

print('\n\nStopwords')

english_stops = set(stopwords.words('english'))    
words = ['I', 'am', 'a', 'writer']
f = [word for word in words if word not in english_stops]
print(f)

print('\nComplete list of supported languages')
from nltk.corpus import stopwords
print(stopwords.fileids())
