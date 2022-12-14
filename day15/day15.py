myFile = open("input_15_1.txt", "r")
#myFile = open("demoinput15.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")