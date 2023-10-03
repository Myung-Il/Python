a = [4,2,5,1,3]

n=len(a)
for i in range(1,n):
    key=a[i]
    pl=0
    pr=i-1

    while pl<=pr:
        pc=(pl+pr)//2
        if a[pc]==key:
            break
        elif a[pc]>key:
            pl=pc+1
        else:
            pr=pc-1

    pd = pc+1 if pl<=pr else pr+1 # 삽입해야 할 위치의 인덱스
    for j in range(i, pd, -1):
        a[j]=a[j-1]

    a[pd]=key
    print(a)