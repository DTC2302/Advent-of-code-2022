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
print(len(sensorsAndBeacons))
beaconPerimiters = []
small = 0
big = 4000000
borders = set()
for i in sensorsAndBeacons:
    dist = abs(i[0][0]-i[1][0]) + abs(i[0][1] - i[1][1])+1
    temp = []
    for j in range(dist+1):
        if (i[0][0]-(dist-j)>=small and i[0][0]-(dist-j)<=big) and (i[0][1]+(j+1)<=big and i[0][1]+(j+1)>=small):
            temp.append((i[0][0]-(dist-j), i[0][1]+(j)))
            borders.add((i[0][0]-(dist-j-1), i[0][1]+(j)))
        if (i[0][0]+(dist-j)>=small and i[0][0]+(dist-j)<=big) and (i[0][1]+(j+1)<=big and i[0][1]+(j+1)>=small):
            temp.append((i[0][0]+(dist-j), i[0][1]+(j)))
            borders.add((i[0][0]+(dist-j-1), i[0][1]+(j)))
        if (i[0][0]-(dist-j)>=small and i[0][0]-(dist-j)<=big) and (i[0][1]-(j+1)<=big and i[0][1]-(j+1)>=small):
            temp.append((i[0][0]-(dist-j), i[0][1]-(j)))
            borders.add((i[0][0]-(dist-j-1), i[0][1]-(j)))
        if (i[0][0]+(dist-j)>=small and i[0][0]+(dist-j)<=big) and (i[0][1]-(j+1)<=big and i[0][1]-(j+1)>=small):
            temp.append((i[0][0]+(dist-j), i[0][1]-(j)))
            borders.add((i[0][0]+(dist-j+1), i[0][1]-(j)))
    if i == sensorsAndBeacons[len(sensorsAndBeacons)//2]:
        print('halfway')
    temp2 = set()
    temp2.update(temp)
    beaconPerimiters.append(temp2)
combined = beaconPerimiters[0]
temp = []
print('done')
for i in beaconPerimiters:
    combined = combined.intersection(i)
    for k in i:
        temp.append(k)
print('unpacked')
moreThanFour = []
amt = dict()
for i in temp:
    if i in amt:
        amt[i] +=1
    else:
        amt[i] = 1
for i in amt:
    if amt[i]>=4:
        print(f'{i}:::::{amt[i]} ')