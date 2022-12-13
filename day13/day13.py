import numpy as np

def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def comparePairs(p1, p2):
    if type(p1) is int and type(p2) is int:
        if p1 == p2:
            return None
        else:
            return p1 < p2
    elif type(p1) is list and type(p2) is list:
        for i, x in enumerate(p1):
            if i > len(p2) - 1:
                return False
            else:
                cp = comparePairs(p1[i], p2[i])
                if cp is not None:
                    return cp
        # if p1 is exhausted
        if len(p1) == len(p2):
            return None
        else:
            return True
    # mixed types
    else:
        if type(p1) is int:
            return comparePairs([p1], p2)
        else:
            return comparePairs(p1, [p2])

myFile = open("input_13_1.txt", "r")
#myFile = open("demoinput13.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")

packets = []
for x in rsDataList:
    if x != "":
        exec(f"packets.append({x})")
r0 = 0
pc = 1
for i in range(0, len(packets)-1, 2):
    match = comparePairs(packets[i], packets[i+1])
    if match is not False:
        r0 += pc
    pc += 1

print(f"Puzzle 1 result: {r0}")

packets.append([[2]])
packets.append([[6]])

# Implement a bubble sort
gSort = False
while (gSort is False):
    gSort = True
    for i in range(0, len(packets)-1, 1):
        sorted = comparePairs(packets[i], packets[i+1])
        if sorted is False:
            packets = swapPositions(packets, i, i+1)
            gSort = False

print(f"Puzzle 2 solution: {(packets.index([[2]])+1)*(packets.index([[6]])+1)}")
print("end")