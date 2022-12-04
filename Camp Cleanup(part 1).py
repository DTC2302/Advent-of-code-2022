with open("input.txt", 'r') as f:
    pairs = f.readlines()
total = 0
for pair in pairs:
    pair = pair.split(',')
    elf1 = pair[0].split('-')
    elf2 = pair[1].split('-')
    if int(elf1[0])<=int(elf2[0]) and int(elf1[1])>=int(elf2[1]):
        total +=1
    elif int(elf2[0])<=int(elf1[0]) and int(elf2[1])>=int(elf1[1]):
        total+=1
print(total)