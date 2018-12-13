from nltk.tokenize import word_tokenize
import os

path = "./testdocument.txt"
testFile = open(path)

bigString = testFile.read()
testFile.close()

#count up the frequency of the words
wordToken = word_tokenize(bigString)
countDict = {}
for words in wordToken:
    if words in countDict:
        countDict[words] = countDict[words] + 1
    else:
        countDict[words] = 1

print(countDict)

