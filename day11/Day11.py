class Monkey:
    def __init__(self, index, items, operand, operation, testN, trueM, falseM):
        self.index = index
        self.items = items
        self.operand = operand
        self.operation = operation
        self.testN = testN
        self.trueM = trueM
        self.falseM = falseM
        self.inspectCount = 0
        self.moduli = []


# opening the file in read mode
import math
myFile = open("input_11_1.txt", "r")
#myFile = open("demoinput11.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")

index = 0
monkeys = []
for i in range(1, len(rsDataList), 7):
    # starting items
    stItems = list(map(int, rsDataList[i][18:].split(", ")))
    operand = rsDataList[i+1].split(" ")[-1]
    if "+" in rsDataList[i+1]:
        operation = "+"
    else:
        operation = "*"
    testN = int(rsDataList[i+2][-2:])
    trueM = int(rsDataList[i+3][-1])
    falseM = int(rsDataList[i+4][-1])
    monkeys.append(Monkey(index, stItems, operand, operation, testN, trueM, falseM))   
    index += 1

part1ic = []
for x in monkeys:
    part1ic.append(0)

# for i in range(20):
#     for j,x in enumerate(monkeys):
#         # create copy of item
#         icopy = x.items.copy()
#         for k, item in enumerate(icopy):
#             monkeys[j].items.remove(item)
#             if x.operand == "old":
#                 item = item*item
#             elif x.operation == "*":
#                 item = item*int(x.operand)
#             else:
#                 item = item+int(x.operand)
#             item = math.floor(item/3)
#             if item % x.testN == 0:
#                 monkeys[x.trueM].items.append(item)
#             else:
#                 monkeys[x.falseM].items.append(item)
#             monkeys[j].inspectCount += 1
#             part1ic[j] += 1
pDividers = [2, 3, 5, 7, 11, 13, 17, 19]

for i, x in enumerate(monkeys):
    for y in x.items:
        tmpList = []
        for z in pDividers:
            tmpList.append(y % z)
        monkeys[i].moduli.append(tmpList)



for i in range(10000):
    print(i)
    for j,x in enumerate(monkeys):
        # create copy of item
        icopy = x.moduli.copy()
        for k, item in enumerate(icopy):
            monkeys[j].moduli.remove(item)
            if x.operand == "old":
                for n,d in enumerate(item):
                    item[n] = item[n]**2
            elif x.operation == "*":
                for n,d in enumerate(item):
                    item[n] = item[n]*int(x.operand)                    
            else:
                for n,d in enumerate(item):
                    item[n] = item[n]+int(x.operand)
            #item = math.floor(item/3)
            # divider cleanup
            icp = item.copy()
            for a, b in enumerate(icp):
                item[a] = item[a] % pDividers[a]
                
            if item[pDividers.index(x.testN)] == 0:
                monkeys[x.trueM].moduli.append(item)
            else:
                monkeys[x.falseM].moduli.append(item)
            monkeys[j].inspectCount += 1
            part1ic[j] += 1

part1ic.sort()
print(f"Part 1 solution: {part1ic[-1]*part1ic[-2]}")        






print("end")