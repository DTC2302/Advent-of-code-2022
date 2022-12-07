with open('input.txt', 'r') as f:
    string = f.read()
length = len(string)
at = -1
for i in range(0, length-4):
    if len(set(string[i:i+4])) == 4:
        at = i+4
        break
print(at)