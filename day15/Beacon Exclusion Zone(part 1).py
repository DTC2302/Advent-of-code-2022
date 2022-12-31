with open('input.txt', 'r') as f:
    lines = f.readlines()
sensorsAndBeacons = []
for i in lines:
    i = i.split()
    sX = ''.join([x for x in i[2] if x.isnumeric() or x == '-'])
    sY = ''.join([x for x in i[3] if x.isnumeric() or x == '-'])
    bX = ''.join([x for x in i[-2] if x.isnumeric() or x == '-'])
    bY = ''.join([x for x in i[-1] if x.isnumeric() or x == '-'])
    sensorsAndBeacons.append([(int(sX), int(sY)), (int(bX), int(bY))])
lineToCheck = 2000000
for i in sensorsAndBeacons[::]:
    dist = abs(i[0][0]-i[1][0]) + abs(i[0][1] - i[1][1])
    if not(i[0][1]-dist<=lineToCheck-1 and i[0][1]+dist>=lineToCheck-1):
        sensorsAndBeacons.remove(i)
print('Input Parsed')
total = 0
taken = set()
for i in sensorsAndBeacons:
    dist = abs(i[0][0]-i[1][0]) + abs(i[0][1] - i[1][1])
    if i[0][1]<lineToCheck:
        dist-=(lineToCheck-i[0][1]-1)
        for j in range(dist):
            taken.add(i[0][0]+j)
            taken.add(i[0][0]-j)
    elif i[0][1]>lineToCheck:
        dist-=(i[0][1]-lineToCheck-1)
        for j in range(dist):
            taken.add(i[0][0]+j)
            taken.add(i[0][0]-j)
    else:
        for j in range(dist):
            taken.add(i[0][0]+j)
            taken.add(i[0][0]-j)
beacons = set()
for i in sensorsAndBeacons:
    if i[1][1] == lineToCheck:
        beacons.add(i[1][0])
print(len(taken)-len(beacons))
