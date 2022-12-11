class monk:
    def __init__(self, items = [] , operator = ['+', 0], test = 0, true = 0, false = 0):
        self.items = items
        self.operator = operator
        self.test = test
        self.true = true
        self.false = false
        self.observed = 0

    def observ(self, item):
        self.observed+=1
        val = item
        self.items.remove(item)
        if self.operator[0] == '+':
            if self.operator[1] == 'old':
                val+=val
            else:
                val+=self.operator[1]
        else:
            if self.operator[1] == 'old':
                val*=val
            else: 
                val*=self.operator[1]
        val//=3
        if val%self.test == 0:
            return [self.true, val]
        return [self.false, val]

    def getItems(self):
        return self.items

    def getObserved(self):
        return self.observed

with open('input.txt', 'r') as f:
    observations = f.read()
monkies = observations.split('\n\n')
numMonkies = len(monkies)
monks = []
for i in monkies:
    i = i.split('\n')
    items = [int(j) for j in i[1][18:].strip().split(', ')]
    i[2] = i[2].split()
    try:
        operators = [i[2][4], int(i[2][5])]
    except:
        operators = [i[2][4], 'old']
    test = int(i[3].strip().split()[-1])
    true = int(i[4].strip().split()[-1])
    false = int(i[5].strip().split()[-1])
    monks.append(monk(items, operators, test, true, false))
for i in range(20):
    for monk in monks:
        for item in monk.getItems()[::]:
            goto = monk.observ(item)
            monks[goto[0]].items.append(goto[1])
for monk in monks:
    print(monk.getObserved())