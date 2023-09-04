import sys
sys.setrecursionlimit(10**6)

def star(s):
    if s==1:
        return '*'

    starL=star(s//3)
    L=[]

    for i in starL:
        L.append(i*3)
    for i in starL:
        L.append(i+' '*(s//3)+i)
    for i in starL:
        L.append(i*3)
    return L

print(*star(int(sys.stdin.readline())),sep='\n')