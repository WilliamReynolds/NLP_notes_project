import os
import sys
import datetime
import matplotlib.pyplot as plt
import nltk
import re
import pickle
import numpy as np 
import math


def main():

	with open('Corpus_Dictionary_outfile-old', 'rb') as fp:
		Corp = pickle.load(fp)

	CorpusInstance = []
		# convert to dictionary

	def Convert(lst): 
		res_dct = {lst[i]: 1 for i in range(0, len(lst))} 
		return res_dct 

	# loops through words in corpus dictionary to test if 
	# they are found in individual subject corpus
	# if so, wordCount is incremented
	# lastly, wordCount is added to an array
	for word in Corp:
		wordCount = 0          
		for dir, sub, files in os.walk('C:\\Users\\monahan-sandbox\\subjectCorpus'):
			for f in files:
				with open('C:\\Users\\monahan-sandbox\\subjectCorpus\\'+f, 'rb') as fp:
					corpusList = pickle.load(fp)
					enter = input("enter")
				try:
					if (corpusList.index(word)):
						wordCount = wordCount + 1
					except:
						pass

		# adds word count for word in corpus dictionary to a instance list
		# eventuall into np array       
		CorpusInstance.append(wordCount)


	IDFvalue = []

	for value in CorpusInstance:
		idf=math.log10(4579/(value+1))
		IDFvalue.append(idf)


	return IDFvalue




