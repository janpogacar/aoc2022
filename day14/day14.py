myFile = open("input_14_1.txt", "r")
#myFile = open("demoinput14.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")