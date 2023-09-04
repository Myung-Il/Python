def qwe(n1,n2,temp):
    if n2 != 0:
        temp = n1
        n1 = n2
        n2 = temp%n2
        return qwe(n1,n2,temp)
    else:
        return n1

for i in range(int(input())):
    a,b = map(int,input().split())
    print(a*b//qwe(a,b,0))


# 유클리드 호제법

# 78696 = 19332 × 4 + 1368
# 19332 = 1368 × 14 + 180
# 1368 = 180 × 7 + 108
# 180 = 108 × 1 + 72
# 108 = 72 × 1 + 36
# 72 = 36 × 2 + 0


# (18696, 19332) (19332, 1368) (1368, 180) (180, 108) (108, 72) (72, 36)