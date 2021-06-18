'''It may be defined as the process of breaking up a piece of text into smaller parts, such as sentences and words. These smaller parts are called tokens. For example, a word is a token in a sentence, and a sentence is a token in a paragraph.'''

import nltk
from nltk.tokenize import word_tokenize, TreebankWordTokenizer, WordPunctTokenizer, sent_tokenize, RegexpTokenizer
# nltk.download()
w = word_tokenize('Tutorialspoint.com proives high quility techical tutorials for free.')
print(w)

print('\nSame process using TreebankWordTokenizer')

Tokenizer_wrd = TreebankWordTokenizer()
p = Tokenizer_wrd.tokenize('This is me puts your hands up')
print(p)

print('\nSame process using WorkPunctTokenizer')
tokenizer = WordPunctTokenizer()
t = tokenizer.tokenize("i can't allow you to go home early")
print(t)

print('\nSame process using sent_tokenize')
text = "Let us understand the difference between sentence & word tokenizer. It's going to be a simple paragraph"
a = sent_tokenize(text)
print(a)

print('\nSame process using RegexpTokenizer (Example-1)')
tokenizer = RegexpTokenizer("[\w']+")
r = tokenizer.tokenize("won't is a contraction")
e = tokenizer.tokenize("can't is a contraction")
print(r, e)

print('\nSame process using RegexpTokenizer (Example-2)')
tokenizer = RegexpTokenizer('/s+', gaps=True)
i = tokenizer.tokenize("won't is a contraction.")
print(i)

print('\nSame process using RegexpTokenizer (Example-3)')
tokenizer = RegexpTokenizer('/s+', gaps=False)
i = tokenizer.tokenize("won't is a contraction")
print(i)
