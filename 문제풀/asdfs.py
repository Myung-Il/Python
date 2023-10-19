import heapq as hq
from collections import deque
from sys import stdin
input = lambda:stdin.readline().rstrip()


def dijkstra():
    d = {node:float('inf') for node in g}
    d[s] = 0
    q = []
    hq.heappush(q,[0,s])

    while q:
        spc,node = hq.heappop(q)
        if d[node]<spc:continue
        for i in g[node]:
            cost = spc+g[node][i]
            if d[i]>cost:
                d[i] = cost
                hq.heappush(q,[cost,i])
    return d


def dfs():
    q = deque([e])
    v = []
    while q:
        x = q.popleft()
        if x==s:continue
        for i in r_g[x]:
            if dg[i]+g[i][x]==dg[x]and [i,x]not in v:
                v.append([i,x])
                q.append(i)
    return v


while 1:
    n,m = map(int,input().split())
    if n==0 and m==0:break
    s,e = map(int,input().split())
    g = {i:dict()for i in range(n)}
    r_g = {i:dict()for i in range(n)}
    for _ in range(m):
        a,b,c = map(int,input().split())
        g[a][b] = c
        r_g[b][a] = c

    dg = dijkstra()
    for i,x in dfs():del g[i][x]
    dg = dijkstra()
    if dg[e]==float('inf'):print(-1)
    else:print(dg[e])