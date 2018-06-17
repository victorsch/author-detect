import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

textone = open("input/one.txt").read()
texttwo = open("input/two.txt").read()

tokenone = word_tokenize(textone)
tokentwo = word_tokenize(texttwo)

trigramone = ngrams(tokenone,3)
trigramtwo = ngrams(tokentwo, 3)

print Counter(trigramone)
print Counter(trigramtwo)
