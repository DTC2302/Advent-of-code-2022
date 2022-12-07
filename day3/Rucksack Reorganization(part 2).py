total = 0
while 1:
    try:
        elf1 = input()
    except EOFError:
        break
    elf2 = input()
    elf3 = input()
    for i in elf1:
        if (i in elf2) and (i in elf3):
            if i.islower():
                total+=(ord(i)-96)
            else:
                total+=(ord(i)-38)
            break
print(total)