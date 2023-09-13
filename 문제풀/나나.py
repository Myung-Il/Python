n = int(input()) # 배열의 크기
k = int(input()) # 찾은려는 배열의 자리값 (1부터)

start = 1 # 찾으려는 값의 최소
end = k   # 찾으려는 값의 최대
r = 0     # 찾으려는 값
while start <= end :        # 찾으려는 값의 탐색 범위
    m = (start + end) // 2  # 중앙값 찾기
    t = 0                   # 찾으려는 값을 예상

    for i in range(1, n+1): # 2차원 배열에서 각 열의 대상
        t += min(m // i, n) # 대상 비교, 찾는 수보다 크면 최대로 고정

    if t < k :              # 예상 수보다 작으면
        start = m + 1       # 최소 라인 끌어 올리기
    elif t >= k :           # 예상 수보다 크거나 같으면
        r = m               # 찾으려는 값으로 수정
        end = m - 1         # 최대 라인 끌어 내리기

print(r) # 찾은 값 출력