import copy

#myFile = open("input_14_1.txt", "r")
myFile = open("demoinput14.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")

coords = []
for x in rsDataList:
    coords.append(x.split(" -> "))

rocks = []
sand = [500,0]

maxY = 0

for x in coords:
    for i in range(len(x)-1):
        x1, y1= eval(x[i])
        x2, y2= eval(x[i+1])

        if (x1==x2) and (y1==y2):
            if [x1, y1] not in rocks:
                rocks.append([x1, y1])
                if y1 > maxY:
                    maxY = y1
        elif (x1==x2):
            llist = [y1, y2]
            llist.sort()
            for j in range(llist[0], llist[1]+1):
                if [x1, j] not in rocks:
                    rocks.append([x1, j])
                    if j > maxY:
                        maxY = j
        else:
            llist = [x1, x2]
            llist.sort()
            for j in range(llist[0], llist[1]+1):
                if [j, y1] not in rocks:
                    rocks.append([j, y1])
                    if y1 > maxY:
                        maxY = y1

rocks2 = copy.deepcopy(rocks)
maxY += 2
count = 0
sandUnit = 0
while(count < 1000):
    if ([sand[0], sand[1]+1] not in rocks):
        sand = [sand[0], sand[1]+1]
        count += 1
    elif [sand[0]-1, sand[1]+1] not in rocks:
        sand = [sand[0]-1, sand[1]+1]
        count += 1
    elif [sand[0]+1, sand[1]+1] not in rocks:
        sand = [sand[0]+1, sand[1]+1]
        count += 1
    else:
        rocks.append(sand)
        sand = [500, 0]
        sandUnit += 1
        count = 0

print(f"Part 1 solution: {sandUnit}")

count = 0
sandUnit = 1
sand = [500,0]

while(count < 1000):
    if ([sand[0], sand[1]+1] not in rocks2) and sand[1]+1 != maxY:
        sand = [sand[0], sand[1]+1]
        count += 1
    elif ([sand[0]-1, sand[1]+1] not in rocks2) and sand[1]+1 != maxY:
        sand = [sand[0]-1, sand[1]+1]
        count += 1
    elif ([sand[0]+1, sand[1]+1] not in rocks2)  and sand[1]+1 != maxY:
        sand = [sand[0]+1, sand[1]+1]
        count += 1
    else:
        if sand == [500, 0]:
            break
        rocks2.append(sand)
        sand = [500, 0]
        sandUnit += 1
        count = 0

print(f"Part 2 solution: {sandUnit}")