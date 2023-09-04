import sys

l = [1]*(10001)
k = 2

while k < 10000:
    if l[k] == 1:
        for i in range(k*2, 10001, k):
            l[i] = 0
    k += 1

l[0],l[1] = 0,0

for i in range(int(sys.stdin.readline().rstrip())):
    a = int(sys.stdin.readline().rstrip())
    k = 0
    
    for j in range(a):
        if l[k] != 0 and l[a-k] != 0 and (a-k) <= a//2:
            break
        k+=1

    print(a-k, k)