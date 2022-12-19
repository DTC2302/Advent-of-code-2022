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
    