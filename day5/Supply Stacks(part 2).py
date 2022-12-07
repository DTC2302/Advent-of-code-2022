with open('input.txt', 'r') as f:
    lines = f.readlines()
numStacks = int(len(lines[0])/4)
stack = -1
for i in lines:
    stack+=1
    if(i[1] == '1'):
        break
stacks = []
for i in range(1, numStacks*4, 4):
    stackX = []
    for j in lines[:stack]:
        stackX.append(j[i])
    stackX = [i for i in stackX if i != ' ']
    stacks.append(stackX)
for i in lines[stack+2:]:
    i = [int(j) for j in i.split() if j.isdigit()]
    for j in range(i[0]-1,-1,-1):
        temp = stacks[i[1]-1].pop(j)
        stacks[i[2]-1].insert(0, temp)
        
out = ''
for i in range(numStacks):
    out = out+stacks[i][0]
print(out)