import heapq

K, N = map(int, input().split())    # 갯수와 위치
p = list(map(int, input().split())) # 요소

q = [] # 힙 트리
m = {} # 방문

for i in range(K):
    heapq.heappush(q, p[i]) # 힙에 요소 충당
    m[p[i]] = 1 # 방문 처리

maximum = p[K-1]  # 최대 값
idx = 0         # 위치 확인

while q:
    cur = heapq.heappop(q) # 최소 값
    idx += 1               # 위치 교체

    if idx == N:           # 종료
        print(cur)
        break

    for i in range(K):
        if len(q) + idx > N and cur * p[i] > maximum: 
            break # 위치보다 멀리가던가 최대보다 클때 정지

        if m.get(cur * p[i], 0) == 1:
            continue # 요소가 들어 있으면 차례 넘김

        m[cur * p[i]] = 1
        heapq.heappush(q, cur * p[i])
        maximum = max(maximum, cur * p[i])
        
    print(q, len(q),idx,len(q)+idx,N)