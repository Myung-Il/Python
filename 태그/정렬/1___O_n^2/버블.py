l=[4,2,5,1,3]

for i in range(4):
    for j in range(4-i):
        if l[j] > l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
    
    print(l)