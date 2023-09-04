import sys
n = int(sys.stdin.readline().rstrip())
l = [[[1]],[[2],[1,1]]] 

# 계단은 한번에 1번에서 2번까지 오를 수 있음
# 계단 1 = [1]
# 계단 2 = [2], [1,1]
# 계단 3 = [2,1], [1,2], [1,1,1]

def qwe(n): # 계단을 오를 수 있는 경우의 수
    if n<=1:
        return 1
    else:
        return qwe(n-1)+qwe(n-2)

for i in range(2,n): # 계단을 오를 수 있는 경우
    l.append([j+[2] for j in l[i-2]] + [j+[1] for j in l[i-1]])
    
print(qwe(n), l[n-1])