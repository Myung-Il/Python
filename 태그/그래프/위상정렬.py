from collections import deque

# 위상정렬
def topology():
    q = deque([])
    r = []
    for i in range(n): # 루트 탐색
        if v[i+1]==0:q.append(i+1)

    while q:
        x = q.popleft() # 루프 출력
        r.append(x)     # 결과에 추가

        for i in g[x]:  # 자식 탐색
            v[i]-=1     # 자식이 아직 봐야할 우선순위가 남아 있다면 넘어감
            if v[i]==0:q.append(i) # 없다면 탐색 범위에 추가
    
    return r

# 메인
if __name__=='__main__':
    n,m = 6,7
    # [[5,6], [5,2], [2,1], [6,1], [2,4], [1,3], [4,3]]
    g = { 1: [ 3   ],
          2: [ 1,4 ],
          3: [     ],
          4: [ 3   ],
          5: [ 6,2 ],
          6: [ 1   ]
        }
    v = [0, 2, 1, 2, 1, 0, 1]

    print(topology())