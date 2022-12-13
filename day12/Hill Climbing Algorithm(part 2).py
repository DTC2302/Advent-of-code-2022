with open(r'C:\Users\darkd\OneDrive\Documents\Code\GitHub\input.txt', 'r') as f:
    lines = f.read()
grid = [[i for i in j] for j in lines.split('\n')]
width = len(grid[0])
verticleHeight = len(grid)
for i in range(len(grid)):
    if 'S' in grid[i]:
        grid[i][grid[i].index('S')] = 'a'
        break
end = (0,0)
for i in range(len(grid)):
    if 'E' in grid[i]:
        end = (i, grid[i].index('E'))
        grid[end[0]][end[1]] = 'z'
        break
find = []
new = []
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'a':
            find.append([(i, j), 0])
            new.append([(i, j), 0])
alpha = 'abcdefghijklmnopqrstuvwxyz'
grid = [[alpha.index(i) for i in line] for line in grid]
notfound = True
while notfound:
    temp = []
    for i in new:  
        at = i[0]
        val = i[1]
        try:
            height = (grid[at[0]][at[1]])
        except IndexError:
            continue
        around = [(at[0]-1, at[1]), (at[0]+1, at[1]), (at[0], at[1]-1), (at[0], at[1]+1)]
        for k in around[::]:
            if k[0]==verticleHeight or k[1]==width:
                around.remove(k)
                continue
            if k[0]<0 or k[1]<0:
                around.remove(k)
                continue
            if (grid[k[0]][k[1]]) > height+1:
                around.remove(k)
                continue
            if any(k in x for x in find):
                around.remove(k)
        if end in around:
            print(val+1)
            notfound = False
            break
        for k in around:
            find.append([k, val+1])
            temp.append([k, val+1])
    new.clear()
    new = temp[::]