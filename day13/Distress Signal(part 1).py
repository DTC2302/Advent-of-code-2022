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
            
            
                    
with open(r'C:\Users\darkd\OneDrive\Documents\Code\GitHub\input.txt', 'r') as f:
    lines = f.readlines()
for i in lines:
    if i == '\n':
        continue
    else:
        lines[lines.index(i)] = eval(i)
total = 0
for i in range(0,len(lines), 3):
    left = lines[i]
    right = lines[i+1]
    a = ordered(left, right)
    if a == True:
        total += (i//3) + 1
    print(total, a)
print(total)