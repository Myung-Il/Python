n,w,h = map(int,input().split())
box = w**2+h**2
for _ in range(n):
    m = int(input())
    if m**2<=box:print('DA')
    else:print('NE')