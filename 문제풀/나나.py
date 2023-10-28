from sys import stdin
input = lambda:stdin.readline().rstrip()


def rangeS(node,start,end,left,right):
    middle = (start+end)//2
    if left>end or start>right:return 0
    if left<=start and end<=right:return tree[node]
    return rangeS(node*2,start,middle,left,right)+rangeS(node*2+1,middle+1,end,left,right)

def update(node,start,end,idx,dif):
    middle = (start+end)//2
    if start>idx or idx>end:return
    if start==end:tree[node] = dif
    else:
        update(node*2,start,middle,idx,dif)
        update(node*2+1,middle+1,end,idx,dif)
        tree[node] = tree[node*2]+tree[node*2+1]


if __name__=='__main__':
    n,k = map(int,input().split())
    tree = [0]*n*4

    for _ in range(k):
        t,a,b = map(int,input().split())
        if t==0:
            if a>b:print(rangeS(1,1,n,b,a))
            else:print(rangeS(1,1,n,a,b))
        else:update(1,1,n,a,b)