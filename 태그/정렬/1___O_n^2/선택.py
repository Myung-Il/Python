l=[4,2,5,1,3]

for i in range(5):
    for j in range(i+1,5):
        if l[i] > l[j]:
            l[i],l[j]=l[j],l[i]

    print(l)