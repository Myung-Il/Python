from sys import stdin,setrecursionlimit
setrecursionlimit(10**9)
input = lambda:stdin.readline().rstrip()


def Dfs(x):
    for i in l[x]:
        if not v[i]:
            ans.append(i)
            v[i] = 1
            Dfs(i)


if __name__=='__main__':
    n = int(input())
    rng = range(1,n+1)
    l = {i:[]for i in rng}

    for _ in range(n-1):
        a,b = map(int,input().split())
        l[a].append(b)
        l[b].append(a)

    choi = list(map(int,input().split()))
    v = {i:0 for i in rng}
    v[1] = 1

    ans = [1]
    rank = [-1 for _ in range(n+1)]
    for i in rng:
        rank[choi[i-1]] = i

    for i in rng:
        l[i] = sorted(l[i],key=lambda x:rank[x])

    Dfs(1)
    print(1 if ans==choi else 0)