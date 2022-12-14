import copy

myFile = open("input_14_1.txt", "r")
#myFile = open("demoinput14.txt", "r")
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
        # draw lines in y dimension
        if (x1==x2):
            llist = [y1, y2]
            # ensure correct order when looping
            llist.sort()
            for j in range(llist[0], llist[1]+1):
                # Avoid duplicates
                if [x1, j] not in rocks:
                    rocks.append([x1, j])
                    # find max Y for part 2
                    if j > maxY:
                        maxY = j
        # draw lines in x dimension
        else:
            llist = [x1, x2]
            # ensure correct order when looping
            llist.sort()
            for j in range(llist[0], llist[1]+1):
                # Avoid duplicates
                if [j, y1] not in rocks:
                    rocks.append([j, y1])
                    # find max Y for part 2
                    if y1 > maxY:
                        maxY = y1

rocks2 = copy.deepcopy(rocks)
maxY += 2
count = 0
sandUnit = 0
lsp = []
# if sand falls beyond part 2 floor, it is deemed to be infinitely cascading
while(count < maxY):
    if ([sand[0], sand[1]+1] not in rocks):
        lsp = sand.copy()
        sand = [sand[0], sand[1]+1]
        count += 1
    elif [sand[0]-1, sand[1]+1] not in rocks:
        lsp = sand.copy()
        sand = [sand[0]-1, sand[1]+1]
        count += 1
    elif [sand[0]+1, sand[1]+1] not in rocks:
        lsp = sand.copy()
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
# create stack of sand particles, for quicker solving
sandList = []

# Give this part some time to compute, at least 30 seconds
while(1):
    if ([sand[0], sand[1]+1] not in rocks2) and sand[1]+1 != maxY:
        # add previous position to stack
        sandList.append(sand)
        sand = [sand[0], sand[1]+1]
    elif ([sand[0]-1, sand[1]+1] not in rocks2) and sand[1]+1 != maxY:
        sandList.append(sand)
        sand = [sand[0]-1, sand[1]+1]
    elif ([sand[0]+1, sand[1]+1] not in rocks2)  and sand[1]+1 != maxY:
        sandList.append(sand)
        sand = [sand[0]+1, sand[1]+1]
    else:
        if sand == [500, 0]:
            break
        rocks2.append(sand)
        # assign last item to sand
        sand = sandList[-1]
        # remove last item from stack
        sandList.pop()
        sandUnit += 1

print(f"Part 2 solution: {sandUnit}")