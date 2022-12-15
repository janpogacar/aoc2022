from scipy.spatial import distance
#myFile = open("input_15_1.txt", "r")
#maxXY = 4000000
#yline = 2000000
# Demoinput start
myFile = open("demoinput15.txt", "r")
maxXY = 20
yline = 10
# Demoinput end
# reading the file
rsData = myFile.read()
# split file at new lines
rsDataList = rsData.split("\n")
# beacons and sensors are ordered lists, so indices correspond
beacons = []
sensors = []

# Code run time is long, about 5 minutes

# parse input
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
# calculate manhattan distances and prepare sets for part 2
for i, sensor in enumerate(sensors):
    mds.append(distance.cityblock(sensor, beacons[i]))
    edgeSets.append(set())

# loop for part 1, loop over sensors
for i, sensor in enumerate(sensors):
    md = distance.cityblock(sensor, beacons[i])
    # check whole y line, to see if there isn't a beacon there
    for x in range(sensor[0]-md, sensor[0]+md+1):
        if ([x,yline] not in beacons) and (distance.cityblock(sensor, [x,yline]) <= md):
            points.add(complex(x,yline))

print(f"Part 1 solution: {len(points)}")

endSet = set()

# find all points on edge of sensor/beacon distances
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

# Two edge sets need to overlap for them to be viable candidates
for i, x in enumerate(edgeSets):
    for j, y in enumerate(edgeSets):
        if i == j:
            break
        else:
            endSet = endSet.union(y.intersection(x))

# loop over viable candidates
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