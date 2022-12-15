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

for i, sensor in enumerate(sensors):
    md = distance.cityblock(sensor, beacons[i])
    for x in range(sensor[0]-md, sensor[0]+md+1):
        y = 2000000
        if (complex(x,y) not in points) and ([x,y] not in beacons) and (distance.cityblock(sensor, [x,y]) <= md):
            points.add(complex(x,y))
            result += 1



print("end")
