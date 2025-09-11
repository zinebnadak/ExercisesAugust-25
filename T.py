a=[]

for i in range (0,10):
    a.append([])
    for j in range (0,10):
        a[i].append((i+1)*(j+1))
print(a)