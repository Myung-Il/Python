l=[4,2,5,1,3]

for i in range(5):
    for j in range(i):
        if l[i] < l[j]:
            l.insert(j,l.pop(i))

    print(l)