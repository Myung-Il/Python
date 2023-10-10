import heapq as hq
from sys import stdin
input = lambda:stdin.readline().rstrip()

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
l.sort(key=lambda x:x[1])

q = []
for p,d in l:
    hq.heappush(q,p)
    if len(q)>d:hq.heappop(q)

print(sum(q))