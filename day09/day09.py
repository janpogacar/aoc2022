# opening the file in read mode
myFile = open("input_09_1.txt", "r")
#myFile = open("demoinput9.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")