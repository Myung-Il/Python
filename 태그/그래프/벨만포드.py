def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph} # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0                               # 시작 값은 0이어야 함

    for _ in range(len(graph)-1):        # 벨만포드는 음수까지 확인하기 때문에 모든 정점에서 최단이 나올 수 있다
        for node in graph:               # 그렇기 때문에 한번 계산하고 다시 한번 더 계산해주면 모든 정점에서
            for neighbor in graph[node]: # 최단을 구하고 그 중에서 가장 작은 것을 최단으로 상정한다
                distance = distances[node]+graph[node][neighbor] # 여기까지의 거리 + 다음까지의 거리
                if distance < distances[neighbor]: # 합의 거리가 기록된 것보다 작다면
                    distances[neighbor] = distance # 갱신
    
    return distances

if __name__=="__main__":
    graph = {
    'A': {'B': -1, 'C':  4},
    'B': {'C':  3, 'D':  2, 'E':  2},
    'C': {},
    'D': {'B':  1, 'C':  5},
    'E': {'D': -3}
    }

    print(bellman_ford(graph, 'A'))