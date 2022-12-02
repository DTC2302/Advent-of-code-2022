elves = []
elf = []
while 1:
    try:
        elf.append(int(input()))
    except ValueError:
        elves.append(elf[::])
        elf.clear()
    except EOFError:
        elves.append(elf[::])
        break
top = 0
topelf = []
second = 0
third = 0
for i in elves:
    if(sum(i)>top):
        top = sum(i)
        topelf = i
elves.remove(topelf)
for i in elves:
    if(sum(i)>second):
        second = sum(i)
        topelf = i
elves.remove(topelf)
for i in elves:
    if(sum(i)>third):
        third = sum(i)
print(top)
print(second)
print(third)
print(sum([top,second,third]))
