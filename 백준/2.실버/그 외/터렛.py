co = int(input())


for i in range(co):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    L = ((x1-x2)**2+(y1-y2)**2)**(1/2)
    R = r1+r2

    if L == 0 and r1 == r2:
        print(-1)
    
    elif L == R:
        print(1)
    
    elif L+r1 == r2 or L+r2 == r1:
        print(1)

    elif L > R or L+r1 < r2 or L+r2 < r1:
        print(0)

    else:
        print(2)