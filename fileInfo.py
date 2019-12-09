import os

fileCount = 0
filesPerDir = []
dirCount = 0

for dir, sub, file in os.walk(".\\"):
	if (len(dir) == 11):
		dirCount = dirCount + 1
		os.chdir(dir)
		for dirs, subs, files in os.walk(os.getcwd()):
			filesPerDir.append(len(files))
			fileCount = fileCount + len(files)
		os.chdir('..')

print("Subject Number: ", dirCount)
print("Number of Notes: ",fileCount)
print("Average Number of Notes: ", fileCount/dirCount)
print("Max Notes: ", max(filesPerDir))
print("Min Notes: ", min(filesPerDir))



				