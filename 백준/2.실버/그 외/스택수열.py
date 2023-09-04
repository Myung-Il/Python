import sys

n = int(sys.stdin.readline().rstrip())
l = [0]*n
for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    l[i] = a

v = 1
mm = [0]
s = ''

for _ in range(n*2):
    if l[0] != mm[-1]:
        mm.append(v)
        v+=1
        s+='+\n'
    else:
        l.pop(0)
        mm.pop()
        s+='-\n'

if len(l) == 0:
    print(s)
else:
    print('NO')