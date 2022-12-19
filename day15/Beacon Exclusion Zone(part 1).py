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

xS = []
yS = []
for i in sensorsAndBeacons:
    xS.append(i[0][0])
    xS.append(i[1][0])
    yS.append(i[0][1])
    yS.append(i[1][1])
xOffset = abs(min(xS))
sensorsAndBeacons = [[(i[0][0]+xOffset, i[0][1]),(i[1][0]+xOffset, i[1][1])] for i in sensorsAndBeacons]
print('Input Parsed')
grid = [['.' for i in range(max(xS) + xOffset+1)] for i in range(max(yS)+1)]
print('empty grid made')
for i in sensorsAndBeacons:
    grid[i[0][1]][i[0][0]] = 'S'
    grid[i[1][1]][i[1][0]] = 'B'
print('Sensors and beacons installed')
for i in sensorsAndBeacons:
    dist = abs(i[0][0]-i[1][0]) + abs(i[0][1] - i[1][1])
    for j in range(dist+1):
        for k in range(dist+1):
            try:
                if grid[i[0][1]+j][i[0][0]+k] == '.':
                    grid[i[0][1]+j][i[0][0]+k] = '#'
            except:
                None
            try:
                if i[0][0]-k>=0:
                    if grid[i[0][1]+j][i[0][0]-k] == '.':
                        grid[i[0][1]+j][i[0][0]-k] = '#'
            except:
                None
            try:
                if i[0][1]-j>=0:
                    if grid[i[0][1]-j][i[0][0]+k] == '.':
                        grid[i[0][1]-j][i[0][0]+k] = '#'
            except:
                None
            try:
                if i[0][1]-j>=0 and i[0][0]-k>=0:
                    if grid[i[0][1]-j][i[0][0]-k] == '.':
                        grid[i[0][1]-j][i[0][0]-k] = '#'
            except:
                None
        dist-=1
print('# placed')
with open('output.txt', 'w') as f:
    for i in grid:
        f.write(''.join(i)+'\n')
total = 0
for i in grid[2000001]:
    if i == '#':
        total+=1
print(total)