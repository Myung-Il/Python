def floyd_warshall():
    dist = [[INF for _ in range(n)] for _ in range(n)]

    # 최단 경로를 담을 것을 dist로 만듬
    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k in range(n):         # 거쳐가는 점
        for i in range(n):     # 시작하는 점
            for j in range(n): # 도착지는 점
                if dist[i][j] > dist[i][k] + dist[k][j]: # 그냥 갔을 때랑 거쳐서 갔을 때 비교
                    dist[i][j] = dist[i][k] + dist[k][j] # 거쳐서가는게 더 빠르면 갱신

    return dist


INF, n = float('inf'), 4
graph = [[  0,   5, INF,  10],
         [INF,   0,   3, INF],
         [INF, INF,   0,   1],
         [INF, INF, INF,   0]]

for row in floyd_warshall():print(row)