'''Following are some use cases of Wordnet −

   1.  It can be used to look up the definition of a word
   2.  We can find synonyms and antonyms of a word
   3.  Word relations and similarities can be explored using Wordnet
   4.  Word sense disambiguation for those words having multiple uses and definitions
'''
from nltk.corpus import wordnet as wn
syn = wn.synsets('dog')[0]
p = syn.name()
print(p)

o = syn.definition()
print(o)

i = syn.examples()
print(i)

print('\n------------------------------------\n')
syn = wn.synsets('dog')[0]
u = syn.hypernyms()
print(u)

y = syn.hypernyms()[0].hyponyms()
print(y)

t = syn.root_hypernyms()
print(t)

print('\n------------------------------------\n')
syn = wn.synsets('dog')[0]
lemmas = syn.lemmas()
print('length of lemmas: ', len(lemmas))
print('1.', lemmas[0])
print('2.', lemmas[1])
print('3.', lemmas[2])

print('\n--------------- Finding Antonyms ---------------\n')

syn1 = wn.synset('good.n.02')
antonym1 = syn1.lemmas()[0].antonyms()[0]
print(antonym1.name())
print('\n', antonym1.synset().definition())

print('\nSecond Example')
syn2 = wn.synset('good.a.01')
antonym2 = syn2.lemmas()[0].antonyms()[0]
print(antonym2.name())
print(antonym2.synset().definition())




































