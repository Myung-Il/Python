from sys import stdin
input = lambda:stdin.readline().rstrip()


def init(node,start,end):
    middle = (start+end)//2
    if start==end:
        tree[node] = l[start]
        return tree[node]
    else:
        tree[node] = init(node*2,start,middle)+init(node*2+1,middle+1,end)
        return tree[node]



if __name__=='__main__':
    n = int(input())
    l = [None]+[int(input())for _ in range(n)]
    tree = [0]*4*n

    init(1,1,n)
    print()
    for i in range(1,n*4):
        print(i,tree[i])


'''
7
2
1
4
5
1
3
3
= 8
'''