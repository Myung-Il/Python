import heapq
from sys import stdin


def heapsort(iterable):
    h = []
    result = []
    
    for v in iterable:
        print(v)
        heapq.heappush(h, -v)
        
    for _ in range(len(h)):
        result.append(-heapq.heappop(h))
    return result


input=stdin.readline

for _ in range(int(input())):
    q=[0]

    for _ in range(int(input())):
        ty,imf=input().split()

        if ty=='I':
            if q:
                q.append(imf)
                continue
            q[0]=int(imf)


        elif ty=='D' and q:
            q=heapsort(q)
            q[0 if imf=='1'else -1].pop()

    print(q)


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
'''