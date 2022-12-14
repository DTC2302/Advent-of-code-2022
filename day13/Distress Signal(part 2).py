import itertools
def ordered(left, right):
    for l,r in zip(left,right):
        if isinstance(l, int) and isinstance(r, int):
            if(r<l):
                return False
            if(l<r):
                return True
        if isinstance(l, list) or isinstance(r, list):
            if not isinstance(l, list):
                l = [l]
            if not isinstance(r, list):
                r = [r]
            b = ordered(l, r)
            if b == None:
                continue
            return b
    if len(left)<len(right):
        return True
    elif len(right)<len(left):
        return False

def advancedSort(x):
    temp = [x.pop(0)]
    for i in x:
        for j in temp:
            if ordered(i, j):
                temp.insert(temp.index(j), i)
                break
        else:
            temp.append(i)
    return temp


with open(r'C:\Users\darkd\OneDrive\Documents\Code\GitHub\input.txt', 'r') as f:
    lines = f.readlines()
for i in lines:
    if i == '\n':
        continue
    else:
        lines[lines.index(i)] = eval(i)
allPackets = [[[2]], [[6]]]
for i in range(0,len(lines), 3):
    allPackets.append(lines[i])
    allPackets.append(lines[i+1])
allPackets = advancedSort(allPackets)
print((allPackets.index([[6]])+1)*(allPackets.index([[2]])+1))
