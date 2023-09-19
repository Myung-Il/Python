import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

xn=[ 0, 0, 1,-1]
yn=[ 1,-1, 0, 0]

col,row=map(int,input().split())

l=[list(map(int,input().split())) for _ in range(col)]
v=[[-1 for _ in range(row)]for _ in range(col)]

def dfs(x,y):
    if y==col-1 and x==row-1:
        return 1

    if v[y][x]!=-1:
        return v[y][x]

    v[y][x]=0
    for i in range(4):
        xi=x+xn[i]
        yi=y+yn[i]
        if 0<=yi<col and 0<=xi<row and l[y][x]>l[yi][xi]:
            v[y][x]+=dfs(xi,yi)

    return v[y][x]

print(dfs(0,0))

'''
3 4
50 45 40 35 30
99 40 99 30 99
99 35 30 25 20
-2

4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
-3

1 1
1
-1

4 4
93 72 61 58
90 73 19 49
85 36 75 13
21 41 45 7
-2

7 7
100 33 58 59 61 31 30
74 31 55 62 70 70 29
73 98 49 47 11 10 36
62 59 56 45 44 8 7
59 58 54 53 41 7 3
56 32 29 18 40 4 3
34 31 26 40 39 73 1
-27
'''