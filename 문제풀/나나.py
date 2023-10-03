mn,mx = map(int,input().split())

cnt = mx-mn+1
l = [1]*cnt
for i in range(2,int(mx**0.5)+1):
    sq = mn//i**2
    while sq*(i**2)<=mx:
        if 0<=sq*(i**2)-mn<=mx-mn:
            l[sq*(i**2)-mn] = 0
        sq += 1

print(sum(l))