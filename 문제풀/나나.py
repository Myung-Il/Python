from sys import stdin
import heapq as hq
input = lambda:stdin.readline().rstrip()

n = int(input())

l = [list(map(int,input().split()))for _ in range(n)]
l.sort()

g = []
hq.heappush(g, l[0][1])
for i in range(1,n):
    if l[i][0]<g[0]:hq.heappush(g,l[i][1])
    else:
        hq.heappop(g)
        hq.heappush(g,l[i][1])

print(len(g))