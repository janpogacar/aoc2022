# opening the file in read mode
myFile = open("input_03_1.txt", "r")
#myFile = open("demoinput_03.txt", "r") # uncomment for demo input
  
# reading the file
rsData = myFile.read()
  
# split file at new lines
rsDataList = rsData.split("\n")

# Split each line into two halves
rsHalves = []
for x in rsDataList:
    rsHalves.append([x[:len(x)//2], x[len(x)//2:]])


result = 0
for x in rsHalves:
    # get a matching item in both halves
    # pop removes a random element, but the set should be one element long 
    item = (set(x[0]).intersection(x[1])).pop()
    # Convert ASCII code to solution code
    if item.islower():
        result+=(ord(item)-ord('a')+1)
    else:
        result+=(ord(item)-ord('A')+27)

print(f"Puzzle 1 result: {result}")

# Part 2
result = 0
# Loop over input, increment loop counter by 3
for i in range(0, len(rsDataList), 3):
    # loop over matching letters in first two stings
    x = ((set(rsDataList[i]).intersection(rsDataList[i+1])).intersection(rsDataList[i+2])).pop()
    # Convert ASCII code to solution code
    if x.islower():
        result+=(ord(x)-ord('a')+1)
    else:
        result+=(ord(x)-ord('A')+27)

print(f"Puzzle 2 result: {result}")
