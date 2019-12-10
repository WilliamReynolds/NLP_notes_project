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

	with open('Corpus_Dictionary_outfile', 'rb') as fp:
		Corp = pickle.load(fp)

	print(len(Corp))	
	CorpusInstance = []
		# convert to dictionary

	# convert into python dictionary format. 
	def Convert(lst): 
		res_dct = {lst[i]: 1 for i in range(0, len(lst))} 
		return res_dct 

	# loops through words in corpus dictionary to test if 
	# they are found in individual subject corpus
	# if so, wordCount is incremented
	# lastly, wordCount is added to an array
	ArrayPosition = 0

	for word in Corp:
		wordCount = 0

		# for figuring out run time position 
		print(ArrayPosition, flush=True)
		ArrayPosition = ArrayPosition + 1

		#print(word)

		fileArrayPosition = 0         
		for dir, sub, files in os.walk('C:\\Users\\monahan-sandbox\\subjectCorpus'):
			for f in files:
				#print (fileArrayPosition)
				fileArrayPosition = fileArrayPosition + 1
				with open('C:\\Users\\monahan-sandbox\\subjectCorpus\\'+f, 'rb') as fp:
					corpusList = pickle.load(fp)
				try:
					if (corpusList.index(word)):
						wordCount = wordCount + 1
				except:
					pass

		# adds word count for word in corpus dictionary to a instance list
		# eventuall into np array       
		CorpusInstance.append(wordCount)
		print(len(CorpusInstance))


	IDFvalue = []

	# 4759 comes the fileInfo.py file that gives
	# the number of files in the corpus. 
	for value in CorpusInstance:
		idf=math.log10(4579/(value+1))
		IDFvalue.append(idf)



	#print (IDFvalue)
	#print(len(IDFvalue))
	#return IDFvalue
	with open('Corpus_Dictionary_IDF', 'wb') as fp:
		pickle.dump(IDFvalue, fp)




main()