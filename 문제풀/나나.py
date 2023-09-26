from collections import deque
from sys import stdin
input = lambda:stdin.readline().rstrip()


def Bfs():
    v = {i:0 for i in rng}
    q = deque([1])
    v[1] = 1

    ans = []
    rank = [-1 for _ in range(n+1)]
    for i in rng:
        rank[choi[i-1]] = i

    for i in rng:
        l[i] = sorted(l[i],key=lambda x:rank[x])

    while q:
        x = q.popleft()
        ans.append(x)
        for i in l[x]:
            if not v[i]:
                v[i] = 1
                q.append(i)

    return (1 if ans==choi else 0)


if __name__=='__main__':
    n = int(input())
    rng = range(1,n+1)
    l = {i:[]for i in rng}

    for _ in range(n-1):
        a,b = map(int,input().split())
        l[a].append(b)
        l[b].append(a)

    choi = list(map(int,input().split()))
    print(Bfs())