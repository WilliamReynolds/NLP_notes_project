import os
import sys
import pickle
import math
import numpy as np 
import re
from Dictionary import ReturnIndividualCorpus, ReturnUnstructuredText


'''
goal is to create a length (len(corpusDictionary)) x height (# of docs)
works out to be ~16000 words, by 4549 tall . 



'''

def main():
	# import IDF values 
	with open('Corpus_Dictionary_IDF', 'rb') as fp:
		IDFvalue = pickle.load(fp)

	for dir, sub, files in os.walk(".\\"):
		if (len(dir) == 11):
			os.chdir(dir)
			dir_name = dir[2:11]
			print(dir_name)
			enter = input("enter")
			# lists and iterates through files
			for dirs, sub, files in os.walk(os.getcwd()):
				for f in files:
					#print(fileCount)
					print("File: ",fileCount, ": ", f, flush=True)
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


main()