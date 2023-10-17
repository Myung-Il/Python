import heapq
n, m = map(int, input().split())




indegree = [0]*(n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
  prev, post = map(int, input().split())
  graph[prev].append(post)
  indegree[post] += 1

heap = []
for i in range(1,n+1):
  if indegree[i]==0:
    heapq.heappush(heap, i)

result = []
while heap:
  value = heapq.heappop(heap)
  result.append(value)
  for i in graph[value]:
    indegree[i] -= 1
    if indegree[i]==0:
      heapq.heappush(heap, i)

for i in result:
  print(i, end=" ")