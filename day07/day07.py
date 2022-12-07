def check_if_equal(list_1, list_2):
    if len(list_1) != len(list_2):
        return False
    return sorted(list_1) == sorted(list_2)

def getTotalSize(folder):
    global recPath
    tmpSize = folder.size
    for x in folderList:
        if (x.name in folder.linked) and check_if_equal(x.path, recPath):
            recPath.append(x.name)
            tmpSize += getTotalSize(x) 
            recPath.pop() 
    return tmpSize

# opening the file in read mode
myFile = open("input_07_1.txt", "r")
#myFile = open("demoinput7.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")

# List of all folders
folderList = []

class Folder:
    name = ""
    size = 0
    linked = []
    totalSize = 0
    path = []

result = 0
folderPath = []
for x in rsDataList:
    # get list of folders
    if " cd " in x:
        folderName = x.split(" cd ")[1]
        if folderName != "..":
            currentFolder = Folder()
            currentFolder.name = folderName
            currentFolder.linked = []
            folderList.append(currentFolder)
            currentFolder.path = folderPath.copy()
            folderPath.append(folderName)
        else:
            folderPath.pop()
    # Get each folder's subfolders
    if "dir" in x:
        subfolder = x.split("dir ")[1]
        currentFolder.linked.append(subfolder)
    # check if it's an integer
    a = x.split(" ")[0]
    if a.isnumeric():
         currentFolder.size += int(a)

names = []
for x in folderList:
    recPath = x.path.copy()
    recPath.append(x.name)
    x.totalSize = getTotalSize(x)

for x in folderList:
    if x.totalSize <= 100000:
        result += x.totalSize

print(f"Puzzle 1 result: {result}") 

spaceFree = 70000000-folderList[0].totalSize
spaceNeeded = 30000000 - spaceFree
result2 = folderList[0].totalSize
tsList = []
for x in folderList:
    tsList.append(x.totalSize)
    if x.totalSize >= spaceNeeded and x.totalSize < result2:
        result2 = x.totalSize

tList = []
for x in folderList:
    if len(x.path) != 0:
        tList.append([x.name, x.path[-1]])

print(f"Puzzle 2 result: {result2}") 