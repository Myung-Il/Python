from sys import stdin
input = lambda:stdin.readline().rstrip()

col, row, n = map(int,input().split())
l = [input()for _ in range(col)]
bl = [[("W"if (idx+p)%2 else "B")for idx in range(n)]for p in range(n)]


mn = float("inf")
t = col-n if col>row else row-n+1
h = (col-n+1 if col-n else 0)+(row-n+1 if row-n else 0)
for li in range(h if h else 1):
    bcnt = 0
    for yi in range(n):
        for xi in range(n):
            if l[yi+li//t][xi+li%t]!=bl[yi][xi]:bcnt+=1
    mn = min(bcnt,  mn)
print(min(mn, col*row-mn))

'''
4 4 3
BBBB
BBBB
BBBW
BBWB

4 4 3
BBBB
BBBB
BBBW
BBWB

8 8 8
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBBBWBW
WBWBWBWB
BWBWBWBW
WBWBWBWB
BWBWBWBW
'''