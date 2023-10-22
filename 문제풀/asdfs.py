from sys import stdin
input = lambda:stdin.readline().rstrip()


def init(node,start,end):
    global mx

    middle = (start+end)//2
    if start==end:
        tree[node] = (l[start][0],l[start][1])
        mx = max(mx,l[start][0]*l[start][1])
        return tree[node]
    else:
        left_x,left_y = init(node*2,start,middle)
        right_x,right_y = init(node*2+1,middle+1,end)

        if left_y==0:tree[node] = (right_x,right_y)
        elif right_y==0:tree[node] = (left_x,left_y)
        else:tree[node] = (left_x+right_x,max(left_y,right_y))

        mx = max(mx,tree[node][0]*tree[node][1])
        return tree[node]



if __name__=='__main__':
    n = int(input())
    l = [None]+[(1,int(input()))for _ in range(n)]
    tree = [0]*4*n

    mx = 0
    init(1,1,n)

    print()
    for i in range(1,4*n):
        print(i,tree[i])
    print('====',mx)