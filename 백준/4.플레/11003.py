from collections import deque
from sys import stdin as s
input=s.readline

n,r=map(int,input().split())
put=list(map(int,input().split()))

l=deque()
for idx in range(n):
    mn=put[idx]

    while l and l[-1]>mn:l.pop()
    l.append(mn)

    if idx>=r and put[idx-r]==l[0]:l.popleft()
    print(l[0],end=' ')