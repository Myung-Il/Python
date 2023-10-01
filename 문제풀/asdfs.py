import sys, heapq
input = sys.stdin.readline

m,n = map(int,input().split())
maze = [list(map(int,list(input().rstrip()))) for _ in range(n)]
visit = [[float('inf')]*m for _ in range(n)]
move = [(0,1),(1,0),(0,-1),(-1,0)]
hq = [(0,0,0)] # cnt,x,y

while hq:
    cnt,x,y = heapq.heappop(hq)
    if x==(n-1) and y==(m-1):
        print(cnt)
        break
    
    for a,b in move:
        dx=x+a; dy=y+b
        if n>dx>=0 and m>dy>=0:
            if maze[dx][dy] == 1:
                if visit[dx][dy] > cnt+1:
                    visit[dx][dy] = cnt+1
                    heapq.heappush(hq,(cnt+1,dx,dy))
            elif visit[dx][dy] > cnt:
                visit[dx][dy] = cnt
                heapq.heappush(hq,(cnt,dx,dy))