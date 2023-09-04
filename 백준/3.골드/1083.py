import sys

k = int(sys.stdin.readline().rstrip())
m = list(map(int, sys.stdin.readline().rstrip().split()))
n = int(sys.stdin.readline().rstrip())
ll = []
while 1:
    l = []
    if n <= 0 or len(m) < 1:
        break
    if m.index(max(m)) == 0:
        a = max(m)
        n += 1
    else:
        l.extend(m[0:n+1])
        a = max(l)
        n -= l.index(a)-1

    m.pop(m.index(a))
    ll.append(a)
    n-=1

ll.extend(m)
for i in ll:
    print(i, end=' ')