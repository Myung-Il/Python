from collections import deque
import sys
sys.setrecursionlimit(10**8)
input=lambda:sys.stdin.readline().rstrip()


def Dfs(start, now, cyc):
    if start==now and cyc>=2:
        return True
    v[now] = True
    for i in l[now]:
        if not v[i]and Dfs(start, i, cyc+1):
            return True
        elif start==i and cyc>=2:
            return True
    return False

def Bfs():
    q = deque([])
    r = [-1]*n
    for i in range(1,n+1):
        if cycle[i]:
            r[i-1] = 0
            q.append(i)

    while q:
        a = q.popleft()
        for i in l[a]:
            if r[i-1]==-1:
                q.append(i)
                r[i-1] = r[a-1] + 1
    return r


if __name__=='__main__':
    n = int(input())
    l = {i:[] for i in range(1,n+1)}
    for _ in range(n):
        a,b = map(int,input().split())
        l[a].append(b)
        l[b].append(a)
    
    cycle = [False]*(n+1)
    for i in range(1,n+1):
        v = [False]*(n+1)
        if Dfs(i, i, 0):
            cycle[i] = True

    print(*Bfs())