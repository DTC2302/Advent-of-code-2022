from inputHandling import read
elves = [[int(k) for k in i.split()] for i in read().split('\n\n')]
print(elves)  
top = 0
for i in elves:
    if(sum(i)>top):
        top = sum(i)
print(top)
