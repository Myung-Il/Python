from collections import deque
import sys
input = lambda:sys.stdin.readline().rstrip()


xn = [1, 0,-1, 0]
yn = [0, 1, 0,-1]
def f(c):
    if c=='L':return(dir-1)%4
    else:return(dir+1)%4


if __name__=='__main__':
    n = int(input())
    bored = [[0]*n for _ in range(n)]
    for _ in range(int(input())):
        y,x = map(int,input().split())
        bored[y-1][x-1] = 4
    bored[0][0] = 1

    d = dict()
    for _ in range(int(input())):
        s,c = input().split()
        d[int(s)] = c

    q = deque([[0,0]])
    x,y = 0,0
    cnt,dir = 0,0
    while 1:
        cnt+=1
        x+=xn[dir];y+=yn[dir]
        if 0>x or x>=n or 0>y or y>=n:break
        
        if bored[y][x]==4:
            bored[y][x] = 1
            q.append([x,y])
            if cnt in d:
                dir = f(d[cnt])

        elif bored[y][x]==0:
            bored[y][x] = 1
            q.append([x,y])
            a,b = q.popleft()
            bored[b][a] = 0
            if cnt in d:
                dir = f(d[cnt])
        
        else:break
    print(cnt)