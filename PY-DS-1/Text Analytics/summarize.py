from textblob import TextBlob, Word
import sys
import random

text = sys.stdin.read()
blob = TextBlob(text)

nouns = list()
for word, tag in blob.tags:
	if tag == 'NN':
		nouns.append(word.lemmatize())

print ("This text is about...")
for item in random.sample(nouns, 10):
	word = Word(item)
	print (word.pluralize())