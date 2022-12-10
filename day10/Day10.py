def logResult(xReg, rValues, pc):
    # part 1 solution reg
    global rList
    # 1-D CRT register for part 2
    global crt
    # Check if part 1 solution
    if (pc+1 in rValues):
        rList.append(xReg)
    # Check if part 2 solution
    if pc % 40 in [xReg-1, xReg, xReg+1]:
        crt[pc] = "█"
    return

# opening the file in read mode
myFile = open("input_10_1.txt", "r")
#myFile = open("demoinput10.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")

# program counter
pc = 0
# register x
xReg = 1
# Results register for part 1
rList = []
# Result indices and multipliers
rValues = [20, 60, 100, 140, 180, 220]

# 1-D CRT register for part 1
crt = []
# Fill CRT with emtpy dots
for i in range(6*40):
    crt.append('░')

for i, x in enumerate(rsDataList):
    # No operation
    if x == "noop":
        logResult(xReg, rValues, pc)
        # Increment program counter
        pc += 1
    # Adition
    else:
        # Split line to get adder
        b = x.split(" ")[1]
        logResult(xReg, rValues, pc)
        # Increment program counter for the first time
        pc += 1
        logResult(xReg, rValues, pc)
        # Make the addition
        xReg += int(b)
        # Increment program counter for the second time time
        pc += 1

print(f"Puzzle 1 result: {sum(a*b for a,b in zip(rList,rValues))}")
print("Puzzle 2 result:")
# Print 2-D array
for i in range(0, len(crt), 40):
    print("".join(crt[i:i+40]))