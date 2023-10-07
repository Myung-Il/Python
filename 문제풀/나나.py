from sys import stdin
import heapq as hq
input = lambda:stdin.readline().rstrip()


left_middle = []
right = []
for _ in range(int(input())):
    n = int(input())

    if len(left_middle)==len(right):
        hq.heappush(left_middle,-n)
    else:hq.heappush(right,n)

    if right and right[0]<-left_middle[0]:
        r_ = hq.heappop(right)
        l_m = hq.heappop(left_middle)
        
        hq.heappush(left_middle,-r_)
        hq.heappush(right,-l_m)
    
    print(-left_middle[0])