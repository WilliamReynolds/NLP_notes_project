import os
import sys
import datetime
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import re
from Dictionary import ReturnIndividualCorpus, ReturnUnstructuredCorpus
import pickle


painWordList=[
'.*pain management.*', 
'.*pending pain.*',
 'until.*pain.*under.*control',
 '.*discharge.*pain.*management.*',
 '.*patient.*extended.*due.*pain.*'
 ]

def ListToString(list):
	newString = ""
	for w in list:
		newString = newString + w + " "
	return newString



# searches for pain language over non-normalized text
def testUnstructured():
	painUnstructured = False
	wordArray = ReturnUnstructuredCorpus()

	SearchString = ListToString(wordArray)

	for p in painWordList:
		if (re.match(p, SearchString)):
			painUnstructured = True
			print(p)
			#enter=input("enter") 
			break 
	print(painUnstructured, flush=True)
	return painUnstructured

# searches for pain language over normalized text
def testStructured():
	painStructured = False
	wordArray = ReturnIndividualCorpus()

	SearchString = ListToString(wordArray)

	for p in painWordList:
		if (re.match(p, SearchString)):
			painUnstructured = True 
			print(p)
			#enter=input("enter") 
			break 
	print(painStructured, flush=True)
	return painStructured






# work through subject corpus and define with boolean

# need to read note and individual corpus. 

subjectPain = []
subjectNoPain = []
dirNumber = 0

for dir, sub, files in os.walk('.\\'):
	print(dirNumber, flush=True)
	dirNumber = dirNumber + 1
	if (len(dir) == 11):
		os.chdir(dir)
		subject=dir[2:11]
		print(dir, flush=True)
		if testStructured() or testUnstructured():
			subjectPain.append(subject)
		else:
			subjectNoPain.append(subject)

		os.chdir('..')


print(len(subjectPain))
with open('SubjectsWithPain', 'wb') as fp:
			pickle.dump(subjectPain, fp)

print(len(subjectNoPain))
with open('SubjectsWithoutPain', 'wb') as fp:
			pickle.dump(subjectNoPain, fp)




