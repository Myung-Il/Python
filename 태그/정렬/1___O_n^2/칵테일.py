l=[4,2,5,1,3]

left = 0
right = len(l)-1
while left<right:
    for i in range(right,left,-1):
        if l[i-1] > l[i]:
            l[i-1],l[i]=l[i],l[i-1]
    left = i
    print(l)

    for i in range(left,right):
        if l[i] > l[i+1]:
            l[i],l[i+1]=l[i+1],l[i]
    right = i
    print(l)