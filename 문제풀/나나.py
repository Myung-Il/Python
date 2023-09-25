import sys, heapq
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
jewelry = [list(map(int,input().split()))for _ in range(n)]
bags = [int(input())for _ in range(m)]

jewelry.sort(reverse=True)
bags.sort()

hq,s = [],0
for i in bags:
    while jewelry:
        w,v = jewelry.pop()
        if w>i:
            jewelry.append([w,v])
            break
        heapq.heappush(hq,[-v,w])
    
    if hq:
        v,w = heapq.heappop(hq)
        if w>i:
            heapq.heappush(hq,[v,w])
            continue
        s-=v
print(s)



'''
3 2
1 65
5 23
2 99
10
2
= 164

4 4
2 1
2 2
2 3
2 4
1
1
2
2
= 7
'''