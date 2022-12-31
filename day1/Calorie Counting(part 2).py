from inputHandling import read
def findTop(elves):
    for i in elves:
        top = 0
        if(sum(i)>top):
            top = sum(i)
            topelf = i
    return topelf

elves = [[int(k) for k in i.split()] for i in read().split('\n\n')]
top = sum(findTop(elves))
elves.remove(findTop(elves))
second = sum(findTop(elves))
elves.remove(findTop(elves))
third = sum(findTop(elves))
print(top)
print(second)
print(third)
print(sum([top,second,third]))
