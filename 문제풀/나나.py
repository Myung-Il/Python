from sys import stdin
input = lambda:stdin.readline().rstrip()


def output(node,start,end,rank):
    middle = (start+end)//2
    if start==end:return start
    if tree[node*2]>=rank:return output(node*2,start,middle,rank)
    return output(node*2+1,middle+1,end,rank-tree[node*2])

def update(node,start,end,idx,dif):
    middle = (start+end)//2
    if end<idx or idx<start:return
    tree[node]+=dif
    if start!=end:
        update(node*2, start, middle, idx, dif)
        update(node*2+1, middle+1, end, idx, dif)
            

if __name__=='__main__':
    n = int(input())
    c = 1_000_001
    tree = [0]*c*4
    
    for _ in range(n):
        t,*i = map(int,input().split())

        if t==1:
            elm = output(1,1,c,i[0])
            print(elm)
            update(1,1,c,elm,-1)
        if t==2:update(1,1,c,i[0],i[1])