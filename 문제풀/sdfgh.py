from sys import stdin
input = lambda:stdin.readline().rstrip()


d = [input() for _ in range(int(input()))]
d_n = {}
for i in d:
    for j in range(len(i)):
        if i[j] in d_n:d_n[i[j]] += 10**(len(i)-j-1)
        else:d_n[i[j]] = 10**(len(i)-j-1)
    
l = []
for i in d_n.values():l.append(i)
l.sort()

s = 0
for i in range(9,-1,-1):
    if not l:break
    s+=l.pop()*i

print(s)