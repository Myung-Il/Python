from sys import stdin
input = lambda:stdin.readline().rstrip()

def init(node, start, end):
    middle = (start+end)//2
    if start==end:tree[node] = l[start]
    else:tree[node] = init(node*2, start, middle)+init(node*2+1, middle+1, end)
    return tree[node]

def lazy(node, start, end):
    if z[node]:
        tree[node] += (end-start+1)*z[node]
        if start!=end:
            z[node*2] += z[node]
            z[node*2+1] += z[node]
        z[node] = 0

def update(node, start, end, left, right, diff):
    lazy(node, start, end)
    middle = (start+end)//2
    if end<left or right<start:return
    if left<=start and end<=right:
        tree[node] += (end-start+1)*diff
        if start!=end:
            z[node*2] += diff
            z[node*2+1] += diff
        return
    update(node*2, start, middle, left, right, diff)
    update(node*2+1, middle+1, end, left, right, diff)
    tree[node] = tree[node*2]+tree[node*2+1]

def rangeSum(node, start, end, x):
    lazy(node, start, end)
    middle = (start+end)//2
    if x<start or end<x:return 0
    if start==end==x:return tree[node]
    rs = rangeSum(node*2, start, middle, x)
    ls = rangeSum(node*2+1, middle+1, end, x)
    return rs+ls


if __name__=='__main__':
    n = int(input())
    l = [0]+list(map(int,input().split()))
    z = [0]*n*4
    tree = [0]*n*4

    init(1,1,n)
    for _ in range(int(input())):
        t,*c = list(map(int,input().split()))
        if t==1:update(1,1,n,c[0],c[1],c[2])
        elif t==2:print(rangeSum(1,1,n,c[0]))