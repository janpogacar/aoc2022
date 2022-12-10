# opening the file in read mode
myFile = open("input_10_1.txt", "r")
#myFile = open("demoinput10.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")

# procgram counter
pc = 1
# register x
xReg = 1
# Results register
rList = []
rValues = [20, 60, 100, 140, 180, 220]

for x in rsDataList:
    if x == "noop":
        if (pc in rValues):
            rList.append(xReg)
        pc += 1
    else:
        a,b = x.split(" ")
        if (pc in rValues):
            rList.append(xReg)
        pc += 1
        if (pc in rValues):
            rList.append(xReg)
        xReg += int(b)
        pc += 1

print(f"Puzzle 1 result: {sum(a*b for a,b in zip(rList,rValues))}")

# procgram counter
pc = 0
# register x
xReg = 1
# Results register
rList = []
rValues = [20, 60, 100, 140, 180, 220]

crt = []
for i in range(6*40):
    crt.append('.')

for i, x in enumerate(rsDataList):
    if x == "noop":
        if pc % 40 in [xReg-1, xReg, xReg+1]:
            crt[pc] = "#"
        pc += 1
    else:
        a,b = x.split(" ")
        if pc % 40 in [xReg-1, xReg, xReg+1]:
            crt[pc] = "#"
        pc += 1
        if pc % 40 in [xReg-1, xReg, xReg+1]:
            crt[pc] = "#"
        xReg += int(b)
        pc += 1

print("Puzzle 2 result:")
for i in range(0, len(crt), 40):
    print("".join(crt[i:i+40]))
