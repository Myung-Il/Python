from sys import stdin
input = lambda:stdin.readline().rstrip()


def init(node,start,end):
    middle = (start+end)//2
    if start==end:tree[node] = [l[start],start]
    else:tree[node] = min(init(node*2,start,middle),init(node*2+1,middle+1,end))
    return tree[node]

def rangeS(node,start,end,left,right):
    middle = (start+end)//2
    if left>end or start>right:return [float('inf')]
    if left<=start and end<=right:return tree[node]
    return min(rangeS(node*2,start,middle,left,right),rangeS(node*2+1,middle+1,end,left,right))

def update(node,start,end,idx,dif):
    middle = (start+end)//2
    if start>idx or idx>end:return
    if start==end:tree[node][0] = dif
    else:
        update(node*2,start,middle,idx,dif)
        update(node*2+1,middle+1,end,idx,dif)
        tree[node] = min(tree[node*2],tree[node*2+1])


if __name__=='__main__':
    n = int(input())
    l = [0]+list(map(int,input().split()))
    tree = [0]*n*4

    init(1,1,n)
    for _ in range(int(input())):
        t,a,b = map(int,input().split())
        if t==2:print(rangeS(1,1,n,a,b)[1])
        else:update(1,1,n,a,b)