import heapq,sys
sys.setrecursionlimit(10**9)
input = lambda:sys.stdin.readline().rstrip()


xn = [ 0, 0, 1,-1]
yn = [ 1,-1, 0, 0]
def Bfs():
    hq = [[0,0,0]]
    v = [[float('inf')]*row for _ in range(col)]

    while hq:
        x,y,bk = heapq.heappop(hq)
        if x==row-1 and y==col-1:
            return bk
        
        for i in range(4):
            xi = x + xn[i]
            yi = y + yn[i]
            if 0<=xi<row and 0<=yi<col:
                if l[yi][xi]==1:
                    if v[yi][xi] > bk+1:
                        v[yi][xi] = bk+1
                        heapq.heappush(hq,[xi,yi,bk+1])
                elif v[yi][xi] > bk:
                    v[yi][xi] = bk
                    heapq.heappush(hq,[xi,yi,bk])


if __name__=='__main__':
    row,col = map(int,input().split())
    l = [list(map(int,list(input())))for _ in range(col)]

    print(Bfs())