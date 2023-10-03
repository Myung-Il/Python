l = [4,2,5,1,3]

n = len(l)
for i in range(1,n):
    key = l[i]
    left = 0
    right = i-1

    while left<=right:
        middle = (left+right)//2
        if l[middle]==key:
            break
        elif l[middle]<key:
            left = middle+1
        else:
            right = middle-1

    ins = middle+1 if left<=right else right+1
    for j in range(i,ins,-1):
        l[j] = l[j-1]
    
    l[ins] = key
    print(l)