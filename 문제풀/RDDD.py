from sys import stdin
input = lambda:stdin.readline().rstrip()

n,k = map(int,input().split())
a,b = [0],[0]
for w in map(int,input().split()):
    if w>0:a.append(w)
    if w<0:b.append(-w)

a.sort(reverse=True)
b.sort(reverse=True)

s = 0
for i in range(0,len(a),k):s+=a[i]*2
for i in range(0,len(b),k):s+=b[i]*2
print(s-max(max(a),max(b)))