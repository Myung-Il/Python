import sys
input = lambda:sys.stdin.readline()
print = lambda x:sys.stdout.write(str(x)+'\n')

N=int(input())
A=sorted([[int(input()),i]for i in range(N)])

l=[0]*N
for i in range(N):
    l[i] = A[i][1] - i

print(max(l)+1)