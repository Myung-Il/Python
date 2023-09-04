import sys

q,w = map(int, sys.stdin.readline().rstrip().split())

if q == 1:
    q = 2

t=True

for i in range(q,w+1):
    b = int(i**0.5)

    for j in range(2, b+1):
        if i%j == 0:
            t=False
            break

    if t:
        print(i)
        
    t=True