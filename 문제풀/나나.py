from sys import stdin
input = lambda:stdin.readline().rstrip()

def init(node, start, end):
    middle = (start+end)//2
    if start==end:
        tree[node] = l[start]
        return tree[node]
    tree[node] = init(node*2, start, middle)+init(node*2+1, middle+1, end)
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

def rangeSum(node, start, end, left, right):
    lazy(node, start, end)
    middle = (start+end)//2
    if end<left or right<start:return 0
    if left<=start and end<=right:return tree[node]
    return rangeSum(node*2, start, middle, left, right)+rangeSum(node*2+1, middle+1, end, left, right)


if __name__=='__main__':
    n,m,k = map(int,input().split())
    l = [0]+[int(input())for _ in range(n)]
    z = [0]*n*4
    tree = [0]*n*4

    init(1,1,n)
    for _ in range(m+k):
        c = list(map(int,input().split()))
        if c[0]==1:update(1,1,n,c[1],c[2],c[3])
        elif c[0]==2:print(rangeSum(1,1,n,c[1],c[2]))

'''
5 2 2
1
2
3
4
5
1 3 4 6
2 2 5
1 1 3 -2
2 2 5
'''