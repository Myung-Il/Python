from datetime import timedelta as td
from time import time, sleep
start = time()


from sys import stdin
input = lambda:stdin.readline().rstrip()


m = [input().split()for _ in range(10)]

r = 0
c = [0]*10
for i in range(10):
    c[i] = len(set(m[i]))
    if c[i]==1:r+=1;break

c = [[]for _ in range(10)]
if r==0:
    for x in range(10):
        for y in range(10):
            c[x].append(m[y][x])
        if len(set(c[x]))==1:r+=1;break

print(r)


end = time()
print(td(seconds=end-start))