import re
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

R_patterns = [
   (r'won\'t', 'will not'),
   (r'can\'t', 'cannot'),
   (r'i\'m', 'i am'),
   (r'(\w+)\'ll', '\g<1> will'),
   (r'(\w+)n\'t', '\g<1> not'),
   (r'(\w+)\'ve', '\g<1> have'),
   (r'(\w+)\'s', '\g<1> is'),
   (r'(\w+)\'re', '\g<1> are'),
]

class REReplacer(object):
    def __init__(self, patterns = R_patterns):
        self.pattern = [(re.compile(regex), repl) for (regex, repl) in patterns]

    def replace(self, text):
        s = text
        for (pattern, repl) in self.pattern:
            s = re.sub(pattern, repl, s)
        return s

rep_word = REReplacer()
pr = rep_word.replace("I won't do it")
print(pr)

re = rep_word.replace("I can't do it")
print(re)

print('\nReplacement before text processing')
rep_word = REReplacer()
q = word_tokenize("I won't be able to do this now")
print(q)

qq = word_tokenize(rep_word.replace("I won't be albe to do this now"))
print(qq)
