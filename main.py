from __future__ import division
import os
import sys
import nltk
from nltk import word_tokenize
from collections import Counter

logName = raw_input("What would you like to name this log?: ")
fileOne = raw_input("Type the name of the first file you'd like to use: ")
fileTwo = raw_input("Type the name of the second file you'd like to use: ")
text = open(fileOne).read()
token = word_tokenize(text)
text2 = open(fileTwo).read()
token2 = word_tokenize(text2)

#Ngram Functions
def ngram(inputToken):
    new = []
    for x in range(0,len(inputToken) - 2):
        new.append(inputToken[x] + ',' + inputToken[x+1] + ',' + inputToken[x+2] + ',')
    return(new)   
def ngram2():
    new = []
    for x in range(0,len(token2) - 2):
        new.append(token2[x] + ',' + token2[x+1] + ',' + token2[x+2] + ',')
    return(new)


#Runs the ngram functions
ngram(token)
ngram2()

#Average Sentence Length Function
def avgsentLength1():
    new = []
    length = len(token)
    sentences = 0
    for x in range(0,len(token) - 2):
        new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',')
        if(token[x+2] == '.'):
            sentences += 1
    return(length/sentences)
def avgsentLength2():
    new = []
    length = len(token2)
    sentences = 0
    for x in range(0,len(token2) - 2):
        new.append(token2[x] + ',' + token2[x+1] + ',' + token2[x+2] + ',')
        if(token2[x+2] == '.'):
            sentences += 1
    return(length/sentences)
print(avgsentLength1())
print(avgsentLength2())



# Average Number of Commas Per Sentece
def avgCommaOne1():
    new = []
    length = len(token)
    commas = 0
    sentences = 0
    for x in range(0,len(token) - 2):
        new.append(token[x] + ',' + token[x+1] + ',' + token[x+2] + ',')
        if(token[x+2] == ','):
            commas += 1
        if(token[x+2] == '.'):
            sentences += 1
    return(commas/sentences)
def avgCommaOne2():
    new = []
    length = len(token2)
    commas = 0
    sentences = 0
    for x in range(0,len(token2) - 2):
        new.append(token2[x] + ',' + token2[x+1] + ',' + token2[x+2] + ',')
        if(token2[x+2] == ','):
            commas += 1
        if(token2[x+2] == '.'):
            sentences += 1
    return(commas/sentences)
print(avgCommaOne1())
print(avgCommaOne2())


f = open("logs/"+logName, "w")

f.write(fileOne)
f.write(" and ")
f.write(fileTwo)
f.write("\n")
f.write("\n")
#Prints the percentage of similarity between the ngrams of text1 and text2
print(list(set(ngram(token)).intersection(ngram2())))
pct_similarity = (len(list(set(ngram(token)).intersection(ngram2()))))/len(ngram2())
print('')
print("\nn-gram Similarity Percentage:")
f.write("n-gram Similarity Percentage:")
print(pct_similarity)
f.write(str(pct_similarity))

#print(len(ngram2())) #prints the length of the text2's ngram

print('') #Puts a space between both comparisons
#Prints the ratio of average sentence length between text1 and text2, the closer to 1, the more likely it is the same author
print("Sentence Length Ratio:")
f.write("\nSentence Length Ratio:")
print(avgsentLength1()/avgsentLength2())
f.write(str(avgsentLength1()/avgsentLength2()))

print('')
print("Average Comma Per Sentence Ratio:")
f.write("\nAverage Comma Per Sentence Ratio:")
print(avgCommaOne1() / avgCommaOne2())
f.write(str(avgCommaOne1() / avgCommaOne2()))

f.close() #Closes the logging file







