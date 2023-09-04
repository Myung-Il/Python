import sys
input = sys.stdin.readline
N = int(input())
g = [list(map(int,input().split())) for _ in range(N)]
MIN = float('inf')
def rec(start,cnt,cur):
    global MIN
    
    MIN = min(MIN,abs(cur))
    if cnt == N//2 :
        return

    for i in range(start,N+1):
        rec(i+1,cnt+1,cur-sum([g[j][i-1]+g[i-1][j] for j in range(N)]))

rec(1,0,sum([sum(g[i]) for i in range(N)]))
print(MIN)