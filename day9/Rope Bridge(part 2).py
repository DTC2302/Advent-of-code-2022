
def moveTail(t,h):
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
    return t

h = [0,0]
n1 = [0,0]
n2 = [0,0]
n3 = [0,0]
n4 = [0,0]
n5 = [0,0]
n6 = [0,0]
n7 = [0,0]
n8 = [0,0]
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
            n1 = moveTail(n1, h)
            n2 = moveTail(n2, n1)
            n3 = moveTail(n3, n2)
            n4 = moveTail(n4, n3)
            n5 = moveTail(n5, n4)
            n6 = moveTail(n6, n5)
            n7 = moveTail(n7, n6)
            n8 = moveTail(n8, n7)
            t = moveTail(t, n8)
            visited.add((t[0], t[1]))
    elif line[0] == 'L':
        for i in range(int(line[1])):
            h[0] -=1
            n1 = moveTail(n1, h)
            n2 = moveTail(n2, n1)
            n3 = moveTail(n3, n2)
            n4 = moveTail(n4, n3)
            n5 = moveTail(n5, n4)
            n6 = moveTail(n6, n5)
            n7 = moveTail(n7, n6)
            n8 = moveTail(n8, n7)
            t = moveTail(t, n8)
            visited.add((t[0], t[1]))
    elif line[0] == 'U':
        for i in range(int(line[1])):
            h[1]+=1
            n1 = moveTail(n1, h)
            n2 = moveTail(n2, n1)
            n3 = moveTail(n3, n2)
            n4 = moveTail(n4, n3)
            n5 = moveTail(n5, n4)
            n6 = moveTail(n6, n5)
            n7 = moveTail(n7, n6)
            n8 = moveTail(n8, n7)
            t = moveTail(t, n8)
            visited.add((t[0], t[1]))
    elif line[0] == 'D':
        for i in range(int(line[1])):
            h[1]-=1
            n1 = moveTail(n1, h)
            n2 = moveTail(n2, n1)
            n3 = moveTail(n3, n2)
            n4 = moveTail(n4, n3)
            n5 = moveTail(n5, n4)
            n6 = moveTail(n6, n5)
            n7 = moveTail(n7, n6)
            n8 = moveTail(n8, n7)
            t = moveTail(t, n8)
            visited.add((t[0], t[1]))
print(len(visited))
            