import heapq as hq
from sys import stdin
input = lambda:stdin.readline().rstrip()


n,t,p = map(int,input().split())
l = list(map(int,input().split()))
q = []

s = 0
for i in range(n):
    hq.heappush(q,-l[i])

    s+=l[i]
    if s>t-i*p and q:
        s-=-hq.heappop(q)
    
print(len(q))