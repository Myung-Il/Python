import heapq

def sol():  # 각 테스트 데이터를 처리하는 함수 정의
    for _ in range(int(input())):
        k = int(input())  # 이번 테스트 데이터에서 수행할 연산의 개수를 입력받음
        min_heap = []  # 오름차순으로 요소를 저장하기 위한 최소 힙을 초기화
        max_heap = []  # 내림차순으로 요소를 저장하기 위한 최대 힙을 초기화
        visited = [False for _ in range(k)]  # 방문 여부를 저장하는 리스트 초기화
        
        # 이번 테스트 데이터에서 각 연산을 처리
        for i in range(k):
            op, num = input().split()  # 연산과 숫자를 입력받음
            num = int(num)
            if op == 'I':  # 연산이 'I' (삽입)인 경우, 숫자를 두 힙에 모두 추가
                heapq.heappush(min_heap, (num, i))
                heapq.heappush(max_heap, (-num, i))
            elif num == -1:  # 연산이 'D -1' (최솟값 삭제)인 경우, 최솟값 삭제
                if min_heap:
                    visited[heapq.heappop(min_heap)[1]] = True
            elif num == 1:  # 연산이 'D 1' (최댓값 삭제)인 경우, 최댓값 삭제
                if max_heap:
                    visited[heapq.heappop(max_heap)[1]] = True
            
            # 힙에서 방문한 요소들을 제거함
            while min_heap and visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            while max_heap and visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
        
        # 만약 최소 힙이 비어있지 않다면, 최댓값과 최솟값을 출력
        if min_heap:
            print(-max_heap[0][0], min_heap[0][0])
        else:  # 최소 힙이 비어있다면 'EMPTY'를 출력
            print('EMPTY')
            
if __name__ == "__main__":
    sol()  # 스크립트가 메인 모듈로 실행되면 'sol()' 함수를 호출