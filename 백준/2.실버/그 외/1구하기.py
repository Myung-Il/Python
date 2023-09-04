import sys
sys.setrecursionlimit(29120)

n = int(sys.stdin.readline().rstrip())
l = [0]*(11)

def qwe(n):
    global l
    if n == 1:
        return 0
    elif l[n] != 0:
        return l[n]

    elif n%6 == 0:
        l[n] = min(qwe(n//3),qwe(n//2))+1
    elif n%3 == 0:
        l[n] = min(qwe(n-1),qwe(n//3))+1
    elif n%2 == 0:
        l[n] = min(qwe(n-1),qwe(n//2))+1
    
    else:
        l[n] = qwe(n-1)+1
    
    return l[n]

print(qwe(n))
print(l)