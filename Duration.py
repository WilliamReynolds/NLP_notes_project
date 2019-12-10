import os
import sys
import datetime
import matplotlib.pyplot as plt
import nltk
import re
import pickle

with open('SubjectsWithPain', 'rb') as fp:
		SubjectWithPain = pickle.load(fp)

with open('SubjectsWithoutPain', 'rb') as fp:
		SubjectWithoutPain = pickle.load(fp)

def lengthTime(dateArray):
	if (len(dateArray) > 1):
		initial = dateArray[0]
		end = dateArray[-1]
		for i in range(0, len(dateArray)):
			if (dateArray[i] < initial): 
				initial = dateArray[i]
			if (dateArray[i] > end):
				end = dateArray[i]

		if(initial == end):
			# creates time object of 1 day for same day patients
			totalTime =  datetime.date(2019, 12, 2) - datetime.date(2019, 12, 1)
		else:
			totalTime = (end-initial)
		totalTime = int(str(totalTime).split(' ')[0])
		return totalTime

def makeNotesLength():
	outputTimeArray=[]
	PainOutputTimeArray=[]
	NoPainOutputTimeArray=[]
	count =0 
	for dir, sub, files in os.walk(".\\"):
		if (len(dir) == 11):
			subjectID = dir[2:11]
			os.chdir(dir)
			for dirs, sub, files in os.walk(os.getcwd()):
				dateArray = []
				for f in files:
					file = open(f, "r")
					line = file.readline()
					#print (line)
					date = line.split('|')[4]
					#print(date)
					date = date.strip()
					year = int(date.split('-')[0])
					month = int(date.split('-')[1])
					day = int(date.split('-')[2])
					dateValue = datetime.date(year, month, day)
					dateArray.append(dateValue)

				if (len(dateArray) > 1):
					totalTime = lengthTime(dateArray)
					outputTimeArray.append(totalTime)
					if (subjectID in SubjectWithPain):
						PainOutputTimeArray.append(totalTime)
					else:
						NoPainOutputTimeArray.append(totalTime)

				file.close()
				os.chdir('..')
	  
		count = count + 1
	return outputTimeArray, PainOutputTimeArray, NoPainOutputTimeArray

def makeStayLength():
	outputTimeArray=[]
	PainOutputTimeArray=[]
	NoPainOutputTimeArray=[]
	count =0 
	for dir, sub, files in os.walk(".\\"):
		if (len(dir) == 11):
			os.chdir(dir)
			subjectID = dir[2:11]
			for dirs, sub, files in os.walk(os.getcwd()):
				dateArray = []
				filePosition = 0
				firstAnes = False
				lastDC = False
				for f in files:
					file = open(f, "r")
					line = file.readline()
					noteType = line.split('|')[6]
					if ((re.match('.*Anes', noteType))):
						firstAnes=True

					# will only loop after first anestiology notes is found
					# until the first DC note is found
					if (firstAnes) and not (lastDC):
						if (re.match('.*Anes', noteType)) or (re.match('.*D/*C', noteType)):
							date = line.split('|')[4]
							#print(date)
							date = date.strip()
							year = int(date.split('-')[0])
							month = int(date.split('-')[1])
							day = int(date.split('-')[2])
							dateValue = datetime.date(year, month, day)
							dateArray.append(dateValue)

						# checks if note was dischared so that while loop
						# won't run anymore. 	
						if (re.match('.*D/*C', noteType)):
							lastDC=True

				if (len(dateArray) > 1):
					totalTime = lengthTime(dateArray)
					outputTimeArray.append(totalTime)
					if (subjectID in SubjectWithPain):
						PainOutputTimeArray.append(totalTime)
					else:
						NoPainOutputTimeArray.append(totalTime)

				file.close()
				os.chdir('..')
	  
		count = count + 1
	return outputTimeArray, PainOutputTimeArray, NoPainOutputTimeArray



def average(timeList):
	sum = 0
	num = 0
	for i in timeList:
		num = num + 1
		sum = sum + i
	print("Subjects: ",num)
	print("MaxDuration: ",max(timeList))
	print("MinDuration: ",min(timeList))

	if (num == 0):
		return 1
	else:
		average = round(sum/num, 2)
		return average

#listAverage = average(outputTimeArray)

#print("\nAverage Stay is " + str(listAverage) + " days.")

def plotAscendingLON(timeList, name):
	avg = average(timeList)
	print(avg)
	timeList.sort()
	for i in range(len(timeList)):
		if (timeList[i] <= avg):
			blueDot, = plt.plot(i, timeList[i], 'bo', label='under', markersize=2)
		elif (timeList[i] > avg):
			redDot, = plt.plot(i, timeList[i], 'ro', label='over', markersize=2)

	avgLine = plt.hlines(avg, 0, len(timeList), colors='b', linestyles='--', label='Line of Average')
	plt.title('Subject Duration of Note Length', fontsize=20)
	plt.xlabel('Subjects', fontsize=15)
	plt.ylabel('Duration of Notes (days)', fontsize=15)
	plt.legend([blueDot, redDot, avgLine], ['Below Average', 'Above Average', 'Average: '+str(avg) + ' days'])

	plt.savefig(name+'.png')
	#plt.show()
	plt.clf()


def plotAscendingLOS(timeList, name):
	avg = average(timeList)
	print(avg)
	timeList.sort()
	for i in range(len(timeList)):
		if (timeList[i] <= avg):
			blueDot, = plt.plot(i, timeList[i], 'bo', label='under', markersize=2)
		elif (timeList[i] > avg):
			redDot, = plt.plot(i, timeList[i], 'ro', label='over', markersize=2)

	avgLine = plt.hlines(avg, 0, len(timeList), colors='b', linestyles='--', label='Line of Average')
	plt.title('Subject Duration of Length 0f Stay', fontsize=20)
	plt.xlabel('Subjects', fontsize=15)
	plt.ylabel('Duration of Stay (days)', fontsize=15)
	plt.legend([blueDot, redDot, avgLine], ['Below Average', 'Above Average', 'Average: '+str(avg) + ' days'])

	plt.savefig(name+'.png')
	#plt.show()
	plt.clf()

#LoN = makeNotesLength()
#LoS = makeStayLength()
LON, PLON, NPLON = makeNotesLength()
LOS, PLOS, NPLOS = makeStayLength()

plotAscendingLON(LON, 'LengthofNotes')
plotAscendingLON(PLON, 'PainLengthofNotes')
plotAscendingLON(NPLON, 'NoPainLengthofNotes')

plotAscendingLOS(LOS, 'LengthofStay')
plotAscendingLOS(PLOS, 'PainLengthofStay')
plotAscendingLOS(NPLOS, 'NoPainLengthofStay')