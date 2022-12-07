with open('input.txt', 'r') as f:
    string = f.read()
length = len(string)
at = -1
for i in range(0, length-14):
    if len(set(string[i:i+14])) == 14:
        at = i+14
        break
print(at)