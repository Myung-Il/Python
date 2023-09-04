import sys
a,b,c=map(int,sys.stdin.readline().rstrip().split())

def A(a,b):
    if b==1:return a%c
    
    m=A(a,b//2)
    
    if not b%2:return (m*m)%c
    else: return (m*m*a)%c

print(A(a,b))