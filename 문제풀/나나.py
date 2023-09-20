from sys import stdin
input=lambda:stdin.readline().rstrip()


def find(u):
    if u!=p[u]:
        p[u]=find(p[u])
    return p[u]


if __name__=='__main__':
    v,e=map(int,input().split())
    l=sorted([list(map(int,input().split()))for _ in range(e)],key=lambda x:x[2])
    p=[i for i in range(v+1)]

    ct=0
    for a,b,c in l:
        rt1=find(a)
        rt2=find(b)
        if rt1!=rt2:
            if rt1>rt2:
                p[rt1]=rt2
            else:
                p[rt2]=rt1
            ct+=c

    print(ct)

'''
3 3
1 2 1
2 3 2
1 3 3
'''