import heapq
import sys

read = sys.stdin.readline

n = int(read().strip("\n"))

lectures = []

for _ in range(n):
    p, d = map(int, read().strip("\n").split())
    lectures.append([p, d])

lectures.sort(key = lambda x: x[1])

queue = []

for pay, day in lectures:
    heapq.heappush(queue, pay)

    if day < len(queue):
        heapq.heappop(queue)

    print(queue)
print(sum(queue))