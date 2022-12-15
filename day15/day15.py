from scipy.spatial import distance
myFile = open("input_15_1.txt", "r")
#myFile = open("demoinput15.txt", "r")
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")
beacons = []
sensors = []

for line in rsDataList:
    a,b = line.split(": closest beacon is at ")
    c, d = b.split(", ")
    exec(c)
    exec(d)
    beacons.append([x,y])
    a = a.split('Sensor at ')[-1]
    c, d = a.split(", ")
    exec(c)
    exec(d)
    sensors.append([x,y])

points = set()
result = 0

edgeSets = []
mds = []
for i, sensor in enumerate(sensors):
    mds.append(distance.cityblock(sensor, beacons[i]))
    edgeSets.append(set())

# for i, sensor in enumerate(sensors):
#     md = distance.cityblock(sensor, beacons[i])
#     for x in range(sensor[0]-md, sensor[0]+md+1):
#         y = 2000000
#         if (complex(x,y) not in points) and ([x,y] not in beacons) and (distance.cityblock(sensor, [x,y]) <= md):
#             points.add(complex(x,y))
#             result += 1

# for x in range(4000000+1):
#     for y in range(4000000+1):
#         # calculate manhatttan distance to sensor
#         allCloser = True
#         for n, sensor in enumerate(sensors):
#             md = distance.cityblock([x,y], sensor)
#             if md <= mds[n]:
#                 allCloser = False
#                 break
#         if allCloser == True:
#             print(4000000*x + y)

endSet = set()

maxXY = 4000000

for i, sensor in enumerate(sensors):
    dx = 0
    for y in range(sensor[1]-mds[i]-1, sensor[1]):
        if y > maxXY or y < 0 or sensor[0]+dx > maxXY or sensor[0]+dx < 0  or sensor[0]-dx > maxXY or sensor[0]-dx < 0:
            dx += 1
            continue
        else:
            edgeSets[i].add(complex(sensor[0]+dx,y))
            edgeSets[i].add(complex(sensor[0]-dx,y))
            dx += 1
    for y in range(sensor[1], sensor[1]+mds[i]+2):
        if y > maxXY or y < 0 or sensor[0]+dx > maxXY or sensor[0]+dx < 0  or sensor[0]-dx > maxXY or sensor[0]-dx < 0:
            dx -= 1
            continue
        else:
            edgeSets[i].add(complex(sensor[0]+dx,y))
            edgeSets[i].add(complex(sensor[0]-dx,y))
            dx -= 1

for i, x in enumerate(edgeSets):
    for j, y in enumerate(edgeSets):
        if i == j:
            break
        else:
            endSet = endSet.union(y.intersection(x))

for x in endSet:
    # calculate manhatttan distance to sensor
    allCloser = True
    for n, sensor in enumerate(sensors):
        md = distance.cityblock([int(x.real),int(x.imag)], sensor)
        if md <= mds[n]:
            allCloser = False
            break
    if allCloser == True:
        print(f"part 2 solution: {int(4000000*x.real + x.imag)}")



print("end")
