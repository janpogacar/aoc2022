# opening the file in read mode
myFile = open("input_04_1.txt", "r")

# reading the file
rsData = myFile.read()
  
# split file at new lines
rsDataList = rsData.split("\n")

result0 = 0
result1 = 0
for x in rsDataList:
    # extract coordinates
    a, b = x.split(",")
    a1, a2 = a.split("-")
    b1, b2 = b.split("-")
    # check for total overlap
    if (int(a1) <= int(b1) and int(a2) >= int(b2)) or (int(b1) <= int(a1) and int(b2) >= int(a2)):
        result0 += 1
        result1 += 1
    # check for partial overlap
    elif (int(b1) >= int(a1) and int(b1) <= int(a2)) or (int(b2) >= int(a1) and int(b2) <= int(a2)):
        result1 += 1

print(f"Puzzle 1 result: {result0}")
print(f"Puzzle 2 result: {result1}")