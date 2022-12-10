with open('input.txt', 'r') as f:
    lines = f.readlines()

def sumCheck():
    global cycle
    global register
    global num
    cycles = [20, 60, 100, 140, 180, 220]
    if cycle in cycles:
        num+=(cycle*register)
    

num = 0
cycle = 1
register = 1
for line in lines:
    if line.strip() == 'noop':
        cycle+=1
        sumCheck()
        continue
    line = line.strip().split()
    cycle+=1
    sumCheck()
    cycle+=1
    register+=int(line[-1])
    sumCheck()
print(num)