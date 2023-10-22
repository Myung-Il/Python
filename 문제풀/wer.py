from sys import stdin
input = lambda:stdin.readline().rstrip()

n = int(input())
r = 0
l,s = [int(input())for _ in range(n)],[]


for i in range(n):
    while s and l[s[-1]]>l[i]:
        h,w = l[s[-1]],i
        s.pop()
        if s:w = i-s[-1]-1
        r = max(r,h*w)
    s.append(i)

while s:
    h,w = l[s[-1]],n
    s.pop()
    if s:w = n-s[-1]-1
    r = max(r,h*w)

print(r)