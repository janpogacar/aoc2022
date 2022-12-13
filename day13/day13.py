import functools

# taken from: https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/
def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

# compare two pairs
def comparePairs(p1, p2):
    # If both inputs are integers
    if type(p1) is int and type(p2) is int:
        if p1 == p2:
            # None return means sort on
            return None
        else:
            return p1 < p2
    elif type(p1) is list and type(p2) is list:
        for i, x in enumerate(p1):
            # if p2 is exhausted
            if i > len(p2) - 1:
                return False
            else:
                cp = comparePairs(p1[i], p2[i])
                # if true or false, return value
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

def wrapPairOutput(p1, p2):
    if comparePairs(p1, p2) is False:
        return 1
    else:
        return -1

myFile = open("input_13_1.txt", "r")
#myFile = open("demoinput13.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")

packets = []
for x in rsDataList:
    if x != "":
        # Since input lines are pythonic lists anyway, we can just exec them
        #exec(f"packets.append({x})")
        packets.append(eval(x))

r0 = 0
pc = 1
# Loop over pais
for i in range(0, len(packets)-1, 2):
    match = comparePairs(packets[i], packets[i+1])
    # If return of comparePairs is none, it needs to be treated as true
    if match is not False:
        r0 += pc
    pc += 1

print(f"Puzzle 1 result: {r0}")

# Append the two values for part 2
packets.append([[2]])
packets.append([[6]])

sortedPackets = sorted(packets, key=functools.cmp_to_key(wrapPairOutput))

print(f"Puzzle 2 solution: {(sortedPackets.index([[2]])+1)*(sortedPackets.index([[6]])+1)}")