from collections import deque
from sys import stdin
input = lambda:stdin.readline().rstrip()


n,k = map(int,input().split())
start = [0]*n
d = {i+1:[]for i in range(n)}
for i in range(k):
    fst,sec = map(int,input().split())
    d[fst].append(sec)
    start[fst-1]+=1

q = deque([])
for i in range(n):
    if len(start[i])==0:q.append(i+1)


while q:
    