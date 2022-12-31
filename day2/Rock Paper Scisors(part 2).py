from inputHandling import *
games = [i.split() for i in readlines()]
score = 0
for i in games:
    if i[1] == 'X':
        if i[0] == 'A':
            score+=3
        elif i[0] == 'B':
            score+=1
        else:
            score+=2
    elif i[1] == 'Y':
        score+=3
        if i[0] == 'A':
            score+=1
        elif i[0] == 'B':
            score+=2
        else:
            score+=3
    elif i[1] == 'Z':
        score+=6
        if i[0] == 'A':
            score+=2
        elif i[0] == 'B':
            score+=3
        else:
            score+=1
print(score)