# define constants for scoring
win = 6
draw = 3
loss = 0

# opening the file in read mode
myFile = open("input_02_1.txt", "r")
  
# reading the file
gameData = myFile.read()
  
# split file at new lines
gameDataList = gameData.split("\n")

# Let's write up all permutations
score = 0

for x in gameDataList:
    # wins
    if x=="A Y" or x=="B Z" or x == "C X":
        score += win
    # draws
    elif x=="A X" or x=="B Y" or x == "C Z":
        score += draw
    # the rest are losses
    # now add the choice score
    if x[2] == "X":
        score += 1
    elif x[2] == "Y":
        score += 2
    elif x[2] == "Z":
        score += 3

# Output the result
print(f"Score after round 1: {score}")

# Part 2
# Reset the score
score = 0
for x in gameDataList:
   # Add the winning scores first
    if x[2] == "X": # loss
        score += loss
        if x[0] == "A":
            score += 3 #rock scissors
        elif x[0] == "B":
            score += 1# Paper rock
        elif x[0] == "C":
            score += 2# scissors paper
    elif x[2] == "Y": # draw
        score += draw
        if x[0] == "A":
            score += 1 #rock rock
        elif x[0] == "B":
            score += 2 # Paper paper
        elif x[0] =="C":
            score += 3 # scissors scissors
    elif x[2] == "Z": # win
        score += win
        if x[0] == "A":
            score += 2 #rock paper
        elif x[0] == "B":
            score += 3# Paper scissors
        elif x[0] == "C":
            score += 1# scissors rock

# Output the result
print(f"Score after round 2: {score}")

    


