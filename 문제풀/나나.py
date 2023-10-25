from sys import stdin,maxsize
input = lambda:stdin.readline().rstrip()


def initMN(node,start,end):
    middle = (start+end)//2
    if start==end:treeMN[node] = l[start]
    else:treeMN[node] = min(initMN(node*2,start,middle),initMN(node*2+1,middle+1,end))
    return treeMN[node]
def rangeMN(node,start,end,left,right):
    middle = (start+end)//2
    if left>end or start>right:return maxsize
    if left<=start and end<=start:return treeMN[node]
    return min(rangeMN(node*2,start,middle,left,right),rangeMN(node*2+1,middle+1,end,left,right))


if __name__=='__main__':
    n,k = map(int,input().split())
    l = [0]+[int(input())for _ in range(n)]
    treeMX = [0]*n*4
    treeMN = [0]*n*4

    initMN(1,1,n)
    for i in range(k):
        a,b = map(int,input().split())
        print(rangeMN(1,1,n,a,b))

'''
10 4
75
30
100
38
50
51
52
20
81
5
1 10
3 5
6 9
8 10
'''