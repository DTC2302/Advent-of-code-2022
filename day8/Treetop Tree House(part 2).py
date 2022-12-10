import time
start_time = time.time()

with open('input.txt', 'r') as f:
    glade = f.readlines()
glade = [[int(i) for i in row.strip()] for row in glade]
gladeHeight = len(glade)
gladeWidth = len(glade[0])
most = 0
for i in range(gladeHeight):
    for j in range(gladeWidth):
        column = [z[j] for z in glade]
        left = 0
        right = 0
        up = 0
        down = 0
        if j>0:
            for k in glade[i][j-1::-1]:
                left+=1
                if k>=glade[i][j]:
                    break
        for k in glade[i][j+1:]:
            right+=1
            if k>=glade[i][j]:
                break
        if i>0:
            for k in column[i-1::-1]:
                up+=1
                if k>=glade[i][j]:
                    break
        for k in column[i+1:]:
            down+=1
            if k>=glade[i][j]:
                break
        if (up * down * left * right)>most:
            most = (up * down * left * right)
print(most)
        

print("Process finished --- %s seconds ---" % (time.time() - start_time))