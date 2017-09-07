from __future__ import division
import nltk
from nltk import word_tokenize
from collections import Counter

text = open("happy.txt").read()
token = word_tokenize(text)
text2 = open("angry.txt").read()
token2 = word_tokenize(text2)


def ngram():
    new = []
    for x in range(0,len(token) - 2):
        new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',')
    return(new)
    
def ngram2():
    new = []
    for x in range(0,len(token2) - 2):
        new.append(token2[x] + ',' + token2[x+1] + ',' + token2[x+2] + ',')
    return(new)

    
ngram()
ngram2()
x = Counter(ngram())
y = Counter(ngram2())

#print(list(set(ngram()).intersection(ngram2())))
pct_similarity = (len(list(set(ngram()).intersection(ngram2()))))/len(ngram2())
print(pct_similarity)
print(len(ngram2()))

