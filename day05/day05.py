import numpy as np
# opening the file in read mode
myFile = open("input_05_1.txt", "r")

# reading the file
rsData = myFile.read()
  
# split file at new lines
rsDataList = rsData.split("\n")

rawStack = rsDataList[0:8]
rawMoves = rsDataList[10:]

cleanMoves = []
# clean up moves
for x in rawMoves:
    tmpMove0 = x[5:].split(" from ")
    tmpMove1, tmpMove2 = tmpMove0[1].split(" to ")
    cleanMoves.append([int(tmpMove0[0]), int(tmpMove1), int(tmpMove2)])

# Clean up stack
cleanStack = []
for x in rawStack:
    tmpRow = []
    for i in range(1, len(x), 4):
        tmpRow.append(x[i])
    cleanStack.append(tmpRow)

mStack = np.transpose(cleanStack)
stack = []
# clean up stack some more
for x in mStack:
    xList = list(x)
    while(" " in xList):
        xList.remove(" ")
    if xList is not None:
        stack.append(xList[::-1])

# Rearrange
for i in range(len(cleanMoves)):
   for j in range(cleanMoves[i][0]):
       stack[cleanMoves[i][2]-1].append(stack[cleanMoves[i][1]-1].pop())

# Print part 1 solution
for x in stack:
    print(x[-1])
    
