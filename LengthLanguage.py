import os
import sys
import datetime
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
import re
from Dictionary import createIndividualCorpus
#import Duration


painWordList=['pain management', 'pending pain', 'pain', ]


for dir, sub, files in os.walk(".\\"):
	for d in dir: 
		subjectArray = createIndividualCorpus(d)
		#subjectArray = []
		match = 0
		for w in subjectArray:	
			for p in painWordList:
				if (re.match(p, w)):
					match = 1
		print(d," is ",match)
		enter = input("enter")


