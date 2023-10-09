import heapq as hq
from sys import stdin
input = lambda:stdin.readline().rstrip()

n = int(input())
l = [list(map(int,input().split()))for _ in range(n)]

l.sort()
q = []
for d,w in l:
    hq.heappush(q,w)
    if d<len(q):hq.heappop(q)
print(sum(q))