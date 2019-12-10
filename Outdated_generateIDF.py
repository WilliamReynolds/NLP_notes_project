import os
import sys
import datetime
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import re
import pickle
from nltk.stem import WordNetLemmatizer



with open('Corpus_Dictionary_outfile', 'rb') as fp:
    item = pickle.load(fp)

    # convert to dictionary

def Convert(lst): 
	res_dct = {lst[i]: 1 for i in range(0, len(lst))} 
	return res_dct 
          

def cleanLine(line):
	#print(line, " lineNumer", lineNumber)
	splits = [':', ',', '.', '/', '-', '[', ']', '(', ')', '\'', '"', '.', '_' ]
	lineSplit = [line]
	for s in splits:
		for l in lineSplit:
			if (len(l.split(s)) > 1):
				for v in (l.split(s)):
					lineSplit.append(v)
				lineSplit.remove(l)

		# steps to clean and normalize
	stopWords = set(stopwords.words('english'))
	cleanedCorpous = []
	tokenCorpus = nltk.tokenize.word_tokenize(corpus)
	lemmatizer = WordNetLemmatizer()

	#creating a cleaned up corpus
	for w in tokenCorpus:
		w = lemmatizer.lemmatize(w)
		cleanedCorpous.append(w)

	# more cleaning, removal using regex as re. 
	patterns = ['.*\/.*', '.*\:,*', '.*\d.*', '.*\~.*', '.*[0-9].*', '\'' ]
	for p in patterns:
		for w in cleanedCorpous:
			if (re.match(p, w)):
				cleanedCorpous.remove(w)

		for w in cleanedCorpous:
			if (re.match('.*\d.*', w)):
				cleanedCorpous.remove(w)

		for w in cleanedCorpous:
			if (re.match('.*\..*', w)):
				cleanedCorpous.remove(w)
		
		for w in cleanedCorpous:
			if (re.match('"', w)):
				cleanedCorpous.remove(w)  

		# to remove seperated out dates and random lettering that won't mean anything
		for w in cleanedCorpous:
			if (len(w) < 3):
				cleanedCorpous.remove(w)

	return   
								


    # load every file
    # parse every word
    	# use dictionary.py code for this. 
def (getTermFreq):
	for dir, sub, files in os.walk(".\\"):
			# stupid work around to make sure only going into correct folders
			if (len(dir) == 11):
				os.chdir(dir)
				#print(dirCount, flush=True)
				print("Directory: ",dirCount, ": ", dir, flush=True)
				dirCount += 1
				# lists and iterates through files
				for dirs, sub, files in os.walk(os.getcwd()):
					for f in files:
						#print(fileCount)
						print("File: ",fileCount, ": ", f, flush=True)
						fileCount += 1
						file = open(f, "r")
						NumLines = sum(1 for line in open(f))
						lineNumber = 0
						while lineNumber <= NumLines:
							# first 10 lines of file are useless header info
							if (lineNumber <= 10):
								file.readline()
							else:
								# create line and iterate through seperating punctuation. 
								line = file.readline().strip().lower()
								lineSplit = cleanLine(line)
								
								# adds the newly seperated texts to the corpus
								for l in lineSplit:
									corpus = corpus + l + " "
							lineNumber = lineNumber + 1
					
						#close file
						file.close()
				os.chdir('..')

