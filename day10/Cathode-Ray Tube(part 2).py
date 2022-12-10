with open('input.txt', 'r') as f:
    lines = f.readlines()

def draw():
    global cycle
    global register
    global num
    lined = [40, 80, 120, 160, 200, 240]
    nums = [register-1, register, register+1]
    if (cycle-1)%40 in nums:
        if cycle in lined:
            return '#\n'
        return '#'
    if cycle in lined:
        return '.\n'
    return '.'
    
    

num = 0
cycle = 1
register = 1
print('#', end = '')
for line in lines:
    if line.strip() == 'noop':
        cycle+=1
        print(draw(), end = '')
        continue
    line = line.strip().split()
    cycle+=1
    print(draw(), end = '')
    cycle+=1
    register+=int(line[-1])
    print(draw(), end = '')
print(num)