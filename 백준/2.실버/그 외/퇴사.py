n = int(input())
l = [0]*n
for i in range(n):
    l[i] = list(map(int,input().split()))

po = [0]*(n+1)
def qwe(n):
    if n == -1:
        return po
    
    if l[n][0]+n <= len(l):
        po[n] = l[n][1] + max(po[l[n][0]+n:])
        return qwe(n-1)
    else:
        po[n] = 0
        return qwe(n-1)
        


print(max(qwe(n-1)))