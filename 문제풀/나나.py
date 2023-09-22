import sys
input = lambda:sys.stdin.readline().rstrip()


def init(node, start, end):
    middle = (start+end)//2
    if start==end:
        tree[node] = l[start]
        return tree[node]
    tree[node] = init(node*2, start, middle)+init(node*2+1, middle+1, end)
    return tree[node]

def update(node, start, end, idx, diff):
    middle = (start+end)//2
    if end<idx or idx<start:return
    tree[node]+=diff
    if start!=end:
        update(node*2, start, middle, idx, diff)
        update(node*2+1, middle+1, end, idx, diff)

def rangeSum(node, start, end, left, right):
    middle = (start+end)//2
    if end<left or right<start:return 0
    if left<=start and end<=right:return tree[node]
    return rangeSum(node*2, start, middle, left, right)+rangeSum(node*2+1, middle+1, end, left, right)


if __name__=='__main__':
    n,m,k = map(int,input().split())
    l = [0]+[int(input()) for _ in range(n)]
    tree = [0]*3_000_000

    init(1, 1, n)
    for _ in range(m+k):
        ty,a,b = map(int,input().split())
        if ty==1:
            diff = b-l[a]
            l[a] = b
            update(1, 1, n, a, diff)
        elif ty==2:
            print(rangeSum(1, 1, n, a, b))