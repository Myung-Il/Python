n=int(input())
a=[int(input())for _ in range(n)]

for i in range(1,n+1):
    changed = False
    for j in range(1,n-i):
        if a[j-1]>a[j]:
            changed = True
            a[j-1],a[j]=a[j],a[j-1]
    if not changed:
        print(i)
        break