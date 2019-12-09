import os
import sys
import pickle
import math
import numpy as np 
import re

'''
goal is to create a length (len(corpusDictionary)) x height (# of docs)
works out to be ~16000 words, by 4549 tall . 



'''

def main():
	with open('Corpus_Dictionary_outfile-old', 'rb') as fp:
		Corp = pickle.load(fp)