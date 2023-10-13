import heapq as hq
from sys import stdin
input = lambda:stdin.readline().rstrip()


k,n = map(int,input().split())
l,q,d = list(map(int,input().split())),[],{}
for elm in l:
    hq.heappush(q,elm)
    d[elm] = 1

mx = max(l)
idx = 1
while 1:
    mn = hq.heappop(q)
    if idx==n:break

    for elm in l:
        if len(q)+idx>n and mn*elm>mx:break
        if d.get(mn*elm,0)==1:continue

        d[mn*elm] = 1
        hq.heappush(q,mn*elm)
        mx = max(mx,mn*elm)

    idx+=1

print(mn)