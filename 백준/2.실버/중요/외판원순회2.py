import sys

n=int(input())
dp=[list(map(int, input().split())) for _ in range(n)]
mi=sys.maxsize

def f(st,nt,s,l):
    global mi
    if len(l)==n and dp[nt][st]!=0:
        mi=min(mi,s+dp[nt][st])
        return

    for i in range(n):
        if dp[nt][i]!=0 and i not in l and s<mi:
            l.append(i)
            f(st,i,s+dp[nt][i],l)
            l.pop()

for i in range(n):
    f(i,i,0,[i])
print(mi)