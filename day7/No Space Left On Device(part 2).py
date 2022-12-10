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
openSpace = 70000000-directories['/']
needed = 30000000-openSpace
directories = list(directories.items())
directories = [(i[0], i[1]) for i in directories if i[1]>=needed]
directories.sort(key = lambda x: x[1])
print(directories[0][1])