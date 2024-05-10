from sys import stdin
input = lambda:stdin.readline().rstrip()

col, row = map(int,input().split())
l = [list(map(int,input()))for _ in range(col)]

mx = 0
for i in range(col):
    for j in range(row):
        if l[i][j]:
            cnt = 0
            while (0<=j-cnt and i+cnt<col)and l[i+cnt][j-cnt]:
                cnt+=1

            for check in range(cnt,0,-1):
                if not l[i+cnt+1][j-cnt+1]:continue
                for idx in range(check):
                    if cnt and(0<=j-cnt+idx+1 and j+cnt-idx-1<row and i+cnt+idx-1<col):
                        if not l[i+idx][j+idx]:cnt = 0
                        if not l[i+cnt+idx-1][j-cnt+idx+1]:cnt = 0
                        if not l[i+cnt+idx-1][j+cnt-idx-1]:cnt = 0
                    else:cnt = 0;break
            mx = max(cnt, mx, 1)


print(mx)

'''
5 5
01100
01011
11111
01111
11111
= 3

3 5
10101
01010
10101
= 2
'''