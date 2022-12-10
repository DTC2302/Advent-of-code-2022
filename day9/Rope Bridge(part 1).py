
def moveTail():
    global h
    global t
    global visited
    if (abs(h[0]-t[0])>1 and abs(h[1]-t[1])>0) or (abs(h[0]-t[0])>0 and abs(h[1]-t[1])>1):
        if h[0]>t[0] and h[1]>t[1]:
            t[0]+=1
            t[1]+=1
        elif h[0]>t[0] and h[1]<t[1]:
            t[0]+=1
            t[1]-=1
        elif h[0]<t[0] and h[1]>t[1]:
            t[0]-=1
            t[1]+=1
        elif h[0]<t[0] and h[1]<t[1]:
            t[0]-=1
            t[1]-=1
    elif abs(h[0]-t[0])>1:
        if h[0]>t[0]:
            t[0]+=1
        else:
            t[0]-=1
    elif abs(h[1]-t[1])>1:
        if h[1]>t[1]:
            t[1]+=1
        else:
            t[1]-=1
    visited.add((t[0], t[1]))


h = [0,0]
t = [0,0]
with open('input.txt', 'r') as f:
    lines = f.readlines()
visited = set()
visited.add((0,0))

for line in lines:
    line = line.strip().split()
    if line[0] == 'R':
        for i in range(int(line[1])):
            h[0] += 1
            moveTail()
    elif line[0] == 'L':
        for i in range(int(line[1])):
            h[0] -=1
            moveTail()
    elif line[0] == 'U':
        for i in range(int(line[1])):
            h[1]+=1
            moveTail()
    elif line[0] == 'D':
        for i in range(int(line[1])):
            h[1]-=1
            moveTail()
print(len(visited))
            