import time
start_time = time.time()

with open('input.txt', 'r') as f:
    glade = f.readlines()
glade = [[int(i) for i in row.strip()] for row in glade]
gladeHeight = len(glade)
gladeWidth = len(glade[0])
visible = set()
for i in range(gladeWidth):
    visible.add((0, i))
    visible.add((gladeHeight-1, i))
for i in range(gladeHeight):
    visible.add((i, 0))
    visible.add((i, gladeWidth-1))
for k in range(gladeHeight):
    row = glade[k]
    for i in range(gladeWidth):
        if all(j<row[i] for j in row[:i]) or all(j<row[i] for j in row[i+1:]):
            visible.add((k,i))

for k in range(0, gladeWidth):
    column = [i[k] for i in glade]
    for i in range(gladeHeight):
        if all(j<column[i] for j in column[:i]) or all(j<column[i] for j in column[i+1:]):
            visible.add((i, k))

print(len(visible))
print("Process finished --- %s seconds ---" % (time.time() - start_time))