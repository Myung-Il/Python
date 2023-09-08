import heapq
from sys import stdin


def heapsort(iterable):
    
    h=[]
    for i in iterable:
        heapq.heappush(h,i)
    for i in range(len(iterable)):
        iterable[i]=heapq.heappop(h)
    
    return iterable


input=stdin.readline

for _ in range(int(input())):
    q=[]

    for _ in range(int(input())):
        ty,imf=input().split()

        if ty=='I':
            q.append(int(imf))

        elif ty=='D' and q:
            q=heapsort(q)
            q.pop(-1 if imf=='1'else 0)

    if q:
        print(max(q),min(q))
    else:
        print('EMPTY')


'''
1
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1

1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333

1
7
I 99
I 98
I 97
D 1
I 96
I 99
D -1
'''