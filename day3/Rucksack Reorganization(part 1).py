total = 0
while 1:
    try:
        items = input()
    except EOFError:
        break
    num = int(len(items)/2)
    comp1 = items[:num]
    comp2 = items[num:]
    for i in comp1:
        if i in comp2:
            if i.islower():
                total+=(ord(i)-96)
            else:
                total+=(ord(i)-38)
            break
print(total)