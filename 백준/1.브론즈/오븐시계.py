a, b = map(int,input().split())
c = int(input())

H = a
M = b + c
while M > 59 :
    H = H + 1
    M = M - 60

while H > 23 :
    H = H - 24

print(H, M)