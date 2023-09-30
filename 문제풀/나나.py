from collections import deque
from sys import stdin,setrecursionlimit
setrecursionlimit(10**9)
input = lambda:stdin.readline().rstrip()


def Bfs():
    q = deque([[n,0]])
    v = [-1]*100_001

    while q:
        x,cnt = q.popleft()
        if x == k:
            break
        
        if -1<x*2<100_001 and v[x*2]==-1:
            v[x*2] = x
            q.append([x*2,cnt])
        if -1<x-1<100_001 and v[x-1]==-1:
            v[x-1] = x
            q.append([x-1,cnt+1])
        if -1<x+1<100_001 and v[x+1]==-1:
            v[x+1] = x
            q.append([x+1,cnt+1])

    return cnt


if __name__=='__main__':
    n,k = map(int,input().split())
    time = Bfs()
    print(time)