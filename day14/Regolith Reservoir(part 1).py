import time
def fall(start, grid):
    pos = (0, start)
    while 1:
        try:
            if grid[pos[0]+1][pos[1]] == '.':
                pos = (pos[0]+1, pos[1])
            elif grid[pos[0]+1][pos[1]-1] == '.':
                pos = (pos[0]+1, pos[1]-1)
            elif grid[pos[0]+1][pos[1]+1] == '.':
                pos = (pos[0]+1, pos[1]+1)
            else:
                break
        except IndexError:
            return None
    grid[pos[0]][pos[1]] = 'o'
    return grid
        
with open('input.txt', 'r') as f:
    lines = f.readlines()
lines = [[(int(j[0:j.index(',')]), int(j[j.index(',')+1:])) for j in line.split(' -> ')] for line in lines]
height = max([tup[1] for line in lines for tup in line]) + 1
horzMin = min([tup[0] for line in lines for tup in line])
horzMax = max([tup[0] for line in lines for tup in line])
length = horzMax-horzMin+1
lines = [[(tup[0]-horzMin, tup[1]) for tup in line] for line in lines] 
area = [['.' for i in range(length)] for i in range(height)]
for line in lines:
    for i in range(len(line)-1):
        start = line[i]
        end = line[i+1]
        if start[0] == end[0]:
            hor = start[0]
            start = start[1]
            end = end[1]
            if start<end:
                for j in range(start, end+1):
                    area[j][hor] = '#'
            else:
                for j in range(start, end-1, -1):
                    area[j][hor] = '#'
        else:
            vert = start[1]
            start = start[0]
            end = end[0]
            if start<end:
                for j in range(start, end+1):
                    area[vert][j] = '#'
            else:
                for j in range(start, end-1, -1):
                    area[vert][j] = '#'
fallStart = 500-horzMin
print(fallStart)
area[0][fallStart] = '+'
pieces = 0
while area != None:
    time.sleep(.1)
    with open('output.txt', 'w') as f:
        try:
            pieces+=1
            area = fall(fallStart, area)
            for i in area:
                f.write(''.join(i) + '\n')
        except:
            print(pieces-1)
