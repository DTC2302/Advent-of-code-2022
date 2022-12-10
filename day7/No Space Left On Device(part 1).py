with open('input.txt', 'r') as f:
    lines = f.readlines()
directories = dict()
current = []
for line in lines:
    line = line.strip().split()
    if line[1] == 'cd':
        if line[2] == '..':
            current.pop()
        else:
            current.append('/'.join(current) + line[2])
    elif line[0].isdigit():
        for i in current:
            if i not in directories:
                directories[i] = int(line[0])
            else:
                directories[i] += int(line[0])
total = 0
for i in directories:
    if directories[i] <=100000:
        total+=directories[i]
print(total)