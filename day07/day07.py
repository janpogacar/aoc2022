# opening the file in read mode
myFile = open("input_07_1.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")