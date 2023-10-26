from sys import stdin
input = lambda:stdin.readline().rstrip()


def init(node,start,end):
    middle = (start+end)//2
    if start==end:tree[node] = l[start]
    else:tree[node] = init(node*2,start,middle)*init(node*2+1,middle+1,end)%1_000_000_007
    return tree[node]

def update(node,start,end,idx,dif):
    middle = (start+end)//2
    if end<idx or idx<start:return 1
    if start==end:tree[node] = dif
    else:
        update(node*2,start,middle,idx,dif)
        update(node*2+1,middle+1,end,idx,dif)
        tree[node] = tree[node*2]*tree[node*2+1]%1_000_000_007

def rangeMtp(node,start,end,left,right):
    middle = (start+end)//2
    if left>end or start>right:return 1
    if left<=start and end<=right:return tree[node]
    return rangeMtp(node*2,start,middle,left,right)*rangeMtp(node*2+1,middle+1,end,left,right)%1_000_000_007


if __name__=='__main__':
    n,m,k = map(int,input().split())
    l = [0]+[int(input())for _ in range(n)]
    tree = [0]*n*4

    init(1,1,n)
    for _ in range(m+k):
        ty,*i = map(int,input().split())
        if ty==1:update(1,1,n,i[0],i[1])
        if ty==2:print(rangeMtp(1,1,n,i[0],i[1]))