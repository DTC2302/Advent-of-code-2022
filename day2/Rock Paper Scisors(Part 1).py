from inputHandling import *
games = [i.split() for i in readlines()]
score = 0
wins = [['A', 'Y'],['B', 'Z'],['C','X']]
ties = [['A', 'X'],['B','Y'],['C','Z']]
for i in games:
    if i[1] == 'X':
        score+=1
    elif i[1] == 'Y':
        score+=2
    else:
        score+=3
    if i in wins:
        score+=6
    elif i in ties:
        score+=3
print(score)