import numpy as np
import copy

def detectUnique(testList, mLen):
    # loop over input data
    for i in range(len(rsData)-mLen):
        # select a subset of a list
        testList = rsData[i:i+mLen]
        # check for uniqueness by creating a set and compating its length
        if (len(set(testList)) == len(testList)):
            # return result and exit function
            return i+mLen

# opening the file in read mode
myFile = open("input_06_1.txt", "r")
# reading the file
rsData = myFile.read()

print(f"Puzzle 1 solution: {detectUnique(rsData, 4)}")
print(f"Puzzle 2 solution: {detectUnique(rsData, 14)}")