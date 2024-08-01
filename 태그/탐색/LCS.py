from sys import stdin
input = lambda:stdin.readline().rstrip()

s1 = "ACAYKP"
s2 = "CAPCAK"

a, b = len(s1)+1, len(s2)+1
dp = [[0]*a for _ in range(b)]
for yi in range(1, b):
    for xi in range(1, a):
        if s1[xi-1]==s2[yi-1]: dp[yi][xi] = dp[yi-1][xi-1]+1 # 접두사 같디면 이전의 결과 +1
        else: dp[yi][xi] = max(dp[yi-1][xi], dp[yi][xi-1])   # 다르다면 최대 값을 가져온다
        
# s1의 최장 부분 수열을 s2에서 찾는 코드 c A p CAK
print(*dp, sep='\n')