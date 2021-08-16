num = 5
num += 1
contex = []
for i in range(1,num):
    tmp = []
    for j in range(1,num):
        tmp.append(j*i)
    contex.append(tmp)
print(contex)
