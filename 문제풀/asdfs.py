import heapq as hq
from sys import stdin
input = lambda:stdin.readline().rstrip()


n = int(input())
l = [list(map(int,input().split()))for _ in range(n)]

l.sort()
q = []

for d,c in l:
    hq.heappush(q,c)
    if len(q)>d:hq.heappop(q)

print(sum(q))