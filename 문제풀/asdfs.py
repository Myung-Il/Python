from collections import deque
from sys import stdin
input = lambda:stdin.readline().rstrip()


if __name__=='__main__':
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    
    l.sort()
    q = deque()
    r,right = float('inf'),1
    for left in range(k):
        if q and q[0]<=left:q.popleft()

        while right<left+n-k:
            while q and l[right]-l[right-1]<=l[q[-1]]-l[q[-1]-1]:q.pop()
            q.append(right)
            right+=1
        
        mn = l[q[0]]-l[q[0]-1]
        mx = l[right-1]-l[left]
        r = min(r,mn+mx)
    print(r)

'''
5 2
-3 -2 3 8 6
= 7

6 2
-5 8 10 1 13 -1
= 13

5 2
0 2 3 9999 10000
= 4
'''