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
for i in elves:
    if(sum(i)>top):
        top = sum(i)
print(top)
