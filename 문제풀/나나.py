from collections import deque
from sys import stdin,setrecursionlimit
setrecursionlimit(10**9)
input = lambda:stdin.readline().rstrip()


def Bfs():
    q = deque([[1,1,1]])
    v = [[True]*1_001 for _ in range(1001)]

    while q:
        x,c_ctrl,cnt = q.popleft()
        if x == n:
            break
        
        if 1<x<1_001 and v[x][x]:
            q.append([x,x,cnt+1])
            v[x][x] = False
        if 1<x+c_ctrl<1_001 and c_ctrl>0 and v[x+c_ctrl][c_ctrl]:
            q.append([x+c_ctrl,c_ctrl,cnt+1])
            v[x+c_ctrl][c_ctrl] = False
        if 1<x-1<1_001 and v[x-1]:
            q.append([x-1,c_ctrl,cnt+1])
            v[x-1][c_ctrl] = False

    return cnt


if __name__=='__main__':
    n = int(input())
    time = Bfs()
    print(time)