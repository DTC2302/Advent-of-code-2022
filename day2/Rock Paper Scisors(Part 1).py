games = []
print('yes')
while 1:
    try:
        games.append(input().split())
    except EOFError:
        break
score = 0
wins = [['A', 'Y'],['B', 'Z'],['C','X']]
ties = [['A', 'X'],['B','Y'],['C','Z']]
for i in games:
    if i[1] == 'X':
        score+=1
    elif i[1] == 'Y':
        score+=2
    elif i[1] == 'Z':
        score+=3
    if i in wins:
        score+=6
    elif i in ties:
        score+=3
print(score)