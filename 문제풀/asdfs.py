import heapq as hq
from sys import stdin
input = lambda:stdin.readline().rstrip()


n = int(input())
l = [list(map(int,input().split()))for _ in range(n)]

l.sort()
q = []

for s,e in l:
    if q and q[0]<=s:hq.heappop(q)
    hq.heappush(q,e)

print(len(q))