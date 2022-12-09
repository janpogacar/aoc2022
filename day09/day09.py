import math
def moveTail(hPos, tPos):
    if (hPos[0] == tPos[0] and hPos[1] == tPos[1]): # if on same position
        return tPos # do not move tail
    elif (math.sqrt((hPos[0]-tPos[0])**2 + (hPos[1]-tPos[1])**2) < 2): # if they are next to or diagonal
        return tPos # do not move tail
    else:
        # if on same column
        if (hPos[0] == tPos[0]):
            if hPos[1] > tPos[1]:
                return [tPos[0], hPos[1]-1]
            else:
                return [tPos[0], hPos[1]+1]
        # if on same row
        elif (hPos[1] == tPos[1]):
            if hPos[0] > tPos[0]:
                return [hPos[0]-1, tPos[1]]
            else:
                return [hPos[0]+1, tPos[1]]
        # if diagonal
        else:
            if (hPos[0] > tPos[0]) and (hPos[1] > tPos[1]):
               return [tPos[0]+1, tPos[1]+1]
            elif (hPos[0] > tPos[0]) and (hPos[1] < tPos[1]):
               return [tPos[0]+1, tPos[1]-1]
            elif (hPos[0] < tPos[0]) and (hPos[1] < tPos[1]):
               return [tPos[0]-1, tPos[1]-1]
            elif (hPos[0] < tPos[0]) and (hPos[1] > tPos[1]):
               return [tPos[0]-1, tPos[1]+1]

def tailPhysics(tails):
    # Puzzle 1 solution
    global tailPositions
    # Puzzle 2 solution
    global endTailPositions
    for i in range(1, len(tails)):
        tails[i] = moveTail(tails[i-1], tails[i])
    if tails[1] not in tailPositions:
        tailPositions.append(tails[1])
    if tails[-1] not in endTailPositions:
        endTailPositions.append(tails[-1])
    return

# opening the file in read mode
myFile = open("input_09_1.txt", "r")
#myFile = open("demoinput9.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")

for i, x in enumerate(rsDataList):
    rsDataList[i] = x.split(" ")

tails = []
# Set up starting condition, head is tail[0]
for i in range(10):
    tails.append([0,0])

tailPositions = []
endTailPositions = []
# head position movements
for x in rsDataList:
    # Right
    if x[0] == 'R':
        for i in range(int(x[1])):
            tails[0][0] += 1
            tailPhysics(tails)
    # Left
    elif x[0] == 'L':
        for i in range(int(x[1])):
            tails[0][0] -= 1
            tailPhysics(tails)
    # Up
    elif x[0] == 'U':
        for i in range(int(x[1])):
            tails[0][1] += 1
            tailPhysics(tails)
    # Down
    elif x[0] == 'D':
        for i in range(int(x[1])):
            tails[0][1] -= 1
            tailPhysics(tails)

print(f"Puzzle 1 solution: {len(tailPositions)}")
print(f"Puzzle 2 solution: {len(endTailPositions)}")