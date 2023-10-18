import heapq as hq
from sys import stdin
input = lambda:stdin.readline().rstrip()


def dijkstra():
    d = {node:[] for node in g}
    d[1].append(0)
    q = []
    hq.heappush(q,[0,1])

    while q:
        spc,node = hq.heappop(q)
        for i in g[node]:
            cost = spc+i[1]
            if len(d[i[0]])<k:
                hq.heappush(d[i[0]], -cost)
                hq.heappush(q, (cost, i[0]))
            elif cost < -d[i[0]][0]:
                hq.heappop(d[i[0]])
                hq.heappush(d[i[0]], -cost)
                hq.heappush(q, (cost, i[0]))
    return d


if __name__=="__main__":
    n,m,k = map(int,input().split())
    g = {i+1:[]for i in range(n)}
    for _ in range(m):
        a,b,c = map(int,input().split())
        g[a].append([b,c])
    
    for i in dijkstra().values():
        print(-(i[0]if len(i)==k else 1))