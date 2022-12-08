import numpy as np
import copy

# opening the file in read mode
myFile = open("input_08_1.txt", "r")
#myFile = open("demoinput8.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")
# Create a 2D list
for i, x in enumerate(rsDataList):
    rsDataList[i] = list(x)

# Create a copy for storing sightlines
scList = copy.deepcopy(rsDataList)
#transpose the 2D list for easier column sleecting
trList = np.transpose(rsDataList)
# Result track for part 1
result = 0

for i, x in enumerate(rsDataList):
    for j, y in enumerate(x):
        # detect edge values first
        if i==0 or i==len(rsDataList)-1 or j==0 or j==len(x)-1:
            result+=1
        # check all lines and columns for larger trees
        # check order: left, right, top, bottom
        elif (all(int(x[j]) > int(z) for z in x[:j])
        or all(int(x[j]) > int(z) for z in x[j+1:])
        or all(int(x[j]) > int(z) for z in trList[j][:i])
        or all(int(x[j]) > int(z) for z in trList[j][i+1:])):
            result += 1

        # Set starting score for part 2
        # if an edge value is detected, the score will remain 0
        if i==0 or i==len(rsDataList)-1 or j==0 or j==len(x)-1:
            sScore = 0
        else:
            sScore = 1
        # left sightline
        tmpScore = 0
        for k, z in enumerate(np.flip(x[:j])):  # flip is needed to ensure correct loop order
            tmpScore += 1
            if int(z) >= int(x[j]):
                break
        sScore = sScore * tmpScore
        tmpScore = 0
        # right sightline
        for k, z in enumerate(x[j+1:]):
            tmpScore +=1
            if int(z) >= int(x[j]):
                break
        sScore = sScore * tmpScore
        tmpScore = 0
        # top sightline
        for k, z in enumerate(np.flip(trList[j][:i])):
            tmpScore +=1
            if int(z) >= int(x[j]):
                break
        sScore = sScore * tmpScore
        tmpScore = 0
        # bottom sightline
        for k, z in enumerate(trList[j][i+1:]):
            tmpScore +=1
            if int(z) >= int(x[j]):
                break
        sScore = sScore * tmpScore
        scList[i][j]=sScore

print(f"Puzzle 1 result:{result}")
# print maximum value for puzzle 2
print(f"Puzzle 2 result:{np.max(scList)}")


