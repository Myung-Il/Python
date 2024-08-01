from sys import stdin
input = lambda:stdin.readline().rstrip()

def bt(e):
    left, right = 0, len(dp)
    while left<right:           # 이분탐색을 이용해서
        mid = (left+right)//2   # e가 갈 수 있는 가장 작은 수쪽으로 보낸다
        if dp[mid]<e:left=mid+1 # ex) 10 7 6 3, e = 5
        else:right=mid          # ex) 10 7 6 5 로 정정
    return right                # 정정될 위치를 반환

n = 12
a = [3, 1, 5, 2, 1, 1, 3, 2, 7, 8, 6]

dp = [-float("inf")]
for idx in range(n-1):
    if dp[-1]<a[idx]:dp.append(a[idx]) # 기존의 값보다 크다면 저장
    else: dp[bt(a[idx])] = a[idx]      # 그게 아니면 검사

    print(dp)