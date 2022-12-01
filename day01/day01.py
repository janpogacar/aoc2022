import numpy as np

# Get calories into a list
# opening the file in read mode
myFile = open("input_01_1.txt", "r")
  
# reading the file
calData = myFile.read()
  
# split file at new lines
calDataList = calData.split("\n")
  
# close the file
myFile.close()

calSums = [] # this will store the calorie values
tmpSum = 0   # temporary sum of each elves' calories

for x in calDataList:
    if x != '':  # Look for blank line
        tmpSum = tmpSum+int(x) 
    else:
        calSums.append(tmpSum)
        tmpSum=0

print("Max calorie sum is %d" %max(calSums)) # Print maximum value
