from collections import deque
import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    if 0<=i<n and 0<=j<n and island[i][j]==1:
        island[i][j]=land_name
        for g in range(4):
            xi=j+xn[g]
            yi=i+yn[g]
            dfs(yi,xi)
        return True
    return False

def bfs(name):
    global bridge
    check=[[-1]*n for _ in range(n)]
    chain=deque([])

    for i in range(n):
        for j in range(n):
            if island[i][j]==name:
                chain.append([j,i])
                check[i][j]=0
    
    while chain:
        x,y=chain.popleft()
        for i in range(4):
            xi=x+xn[i]
            yi=y+yn[i]
            if 0<=xi<n and 0<=yi<n:
                if island[yi][xi]>0 and island[yi][xi]!=name:
                    bridge=min(check[y][x],bridge)
                    return
                if island[yi][xi]==0 and check[yi][xi]==-1:
                    check[yi][xi]=check[y][x]+1
                    chain.append([xi,yi])



n=int(input())
island=[list(map(int,input().split()))for _ in range(n)]

xn=[ 0, 0, 1,-1]
yn=[ 1,-1, 0, 0]

bridge=sys.maxsize

land_name=2
for i in range(n):
    for j in range(n):
        if dfs(i,j):
            land_name+=1

for i in range(2,land_name):
    bfs(i)

print(bridge)