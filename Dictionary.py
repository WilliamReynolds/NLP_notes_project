import os
import sys
import datetime
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import re
import pickle
from nltk.stem import WordNetLemmatizer



customRemoveList = []

def createDictionary():
	print(temp)
	#iterate and merge texts
	#remove stops and filler
	#stem/lem/normilization

def createCohortCorpus():
	# loops through directory files and creates corpus
	# count of 0 = ./ dir which won't work. 
	count =0 
	corpus = ""
	dirCount=0
	fileCount=0
	# list and iterates through subject directories
	for dir, sub, files in os.walk(".\\"):
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
							
							#print(line, " lineNumer", lineNumber)
							splits = [':', ',', '.', '/', '-', '[', ']', '(', ')', '\'', '"', '.', '_', '=' ]
							lineSplit = [line]
							for s in splits:
								for l in lineSplit:
									if (len(l.split(s)) > 1):
										for v in (l.split(s)):
											lineSplit.append(v)
										lineSplit.remove(l)
							
							# adds the newly seperated texts to the corpus
							for l in lineSplit:
								corpus = corpus + l + " "
						lineNumber = lineNumber + 1
				
					#close file
					file.close()
			os.chdir('..')
		count = count + 1

	# steps to clean and normalize
	stopWords = set(stopwords.words('english'))
	cleanedCorpous = []
	tokenCorpus = nltk.tokenize.word_tokenize(corpus)
	lemmatizer = WordNetLemmatizer()

	#creating a cleaned up corpus
	for w in tokenCorpus:
		w = lemmatizer.lemmatize(w)
		if w not in stopWords:
			if w not in cleanedCorpous:
				if w.isalpha():
					cleanedCorpous.append(w)

	# more cleaning, removal using regex as re. 
	patterns = ['.*\/.*', '.*\:,*', '.*\d.*', '.*\~.*', '.*[0-9].*', '\'',  ]
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
			
	cleanedCorpous.sort()
	print(cleanedCorpous) 
	print(len(cleanedCorpous))

	with open('Corpus_Dictionary_outfile', 'wb') as fp:
		pickle.dump(cleanedCorpous, fp)


def createIndividualCorpus():
	count =0 
	dirCount=0
	fileCount=0

	# need to make it folder wide for the corpus
	for dir, sub, files in os.walk('.\\'):
		corpus = ""
		if (len(dir) == 11):
			os.chdir(dir)
			#print(dirCount, flush=True)
			print("Directory: ",dirCount, ": ", dir, flush=True)
			dirCount += 1
			for dir2, sub2, files2 in os.walk('.\\'):
				for f in files2:
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
							splits = [':', ',', '.', '/', '-', '[', ']', '(', ')', '\'', '"', '.', '_' ]
							lineSplit = [line]
							for s in splits:
								for l in lineSplit:
									if (len(l.split(s)) > 1):
										for v in (l.split(s)):
											lineSplit.append(v)
										lineSplit.remove(l)
							
							# adds the newly seperated texts to the corpus
							for l in lineSplit:
								corpus = corpus + l + " "

						lineNumber = lineNumber + 1
					file.close()

			# steps to clean and normalize
			stopWords = set(stopwords.words('english'))
			cleanedCorpous = []
			tokenCorpus = nltk.tokenize.word_tokenize(corpus)
			lemmatizer = WordNetLemmatizer()

			#creating a cleaned up corpus
			for w in tokenCorpus:
				w = lemmatizer.lemmatize(w)
				if w not in stopWords:
					if w not in cleanedCorpous:
						if w.isalpha():
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
					
			cleanedCorpous.sort()
			#print(cleanedCorpous)
			subject = dir[2:len(dir)-1]
			saveDir = 'C:\\Users\\monahan-sandbox\\subjectCorpus\\'
			outFile = saveDir+subject+'_corpus'
			with open(outFile, 'wb') as fp:
				pickle.dump(cleanedCorpous, fp)
			os.chdir('..')

			



#createCohortCorpus()
createIndividualCorpus()