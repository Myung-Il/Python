from collections import deque
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def Dfs(start, here, level, li):
    global cy
    if level <= 2:
        for v in graph[here]:
            if visited[v] == False:
                visited[v] = True
                Dfs(start, v, level+1, li+[v])
                visited[v] = False
    else:
        for v in graph[here]:
            if visited[v] == False:
                visited[v] = True
                Dfs(start, v, level+1, li+[v])
                visited[v] = False
            else:
                if v == start:
                    cy = True
                    for l in li:
                        cycle.add(l)
                    return


def Bfs():
    answer = [int(1e9)] * (n + 1)
    q = deque()
    for c in cycle:
        q.append((c, 0))
        answer[c] = 0

    while q:
        node, level = q.popleft()

        for v in graph[node]:
            if answer[v] == int(1e9):
                answer[v] = level+1
                q.append((v, level+1))
    return answer[1:]


if __name__=='__main__':
    n = int(input())
    graph = [[] for _ in range(n+1)]
    cycle = set()

    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False]*(n+1)
    cy = False
    for i in range(1, n+1):
        if cy == True:
            break
        visited[i] = True
        Dfs(i, i, 1, [i])
        visited[i] = False
    cycle = list(cycle)

    print(*Bfs())