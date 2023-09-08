import heapq

def sol():
    for _ in range(int(input())):
        k = int(input())
        min_heap = []
        max_heap = []
               
        for i in range(k):
            op, num = input().split()
            num = int(num)
            if op == 'I':
                heapq.heappush(min_heap, (num, i))
                heapq.heappush(max_heap, (-num, i))
            elif num == -1:
                if min_heap:
                    heapq.heappop(min_heap)
            elif num == 1:
                if max_heap:
                    heapq.heappop(max_heap)


        if min_heap:
            print(-max_heap[0][0], min_heap[0][0])
        else:
            print('EMPTY')
            
if __name__ == "__main__":
    sol()