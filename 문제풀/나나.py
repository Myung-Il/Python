from sys import stdin
input=lambda:stdin.readline().rstrip()

v,e=map(int,input().split())
l=sorted([list(map(int,input().split()))for _ in range(e)],key=lambda x:x[2])

g=[l.pop(0)]
for i in l:
    a,b,c=i

    