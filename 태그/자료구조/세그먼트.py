def init(node, start, end):   # 노드, 시작, 끝
    middle = (start+end)//2   # 시작과 끝의 중간
    if start==end:            # 시작과 끝이 같다면 밑바닥 자식 노드임
        tree[node] = l[start] # 밑바닥의 범위는 l 리스트를 기준으로 만들어져 있음
        return tree[node]     # 결국 합을 구해야 하니 최소치를 반환
    tree[node] = init(node*2, start, middle)+init(node*2+1, middle+1, end) # 절반씩 자르면서 밑바닥을 찾는 중
    return tree[node]         # 최소치가 아니고 그 다음 합부터는 그냥 반환

def update(node, start, end, idx, diff):           # 노드, 시작, 끝, 바꿔진 인덱스 번호, 합차
    middle = (start+end)//2                        # 시작과 끝의 중간
    if end<idx or idx<start:return                 # 바꿔진 위치를 벗어나면 아무짓도 안함
    tree[node]+=diff                               # 루트는 모든 정점의 합이니 먼저 합차를 더해줌
    if start!=end:                                 # 바꿔진 위치를 못 찾으면 계속
        update(node*2, start, middle, idx, diff)   # 앞쪽 절반에서 찾아보는 중
        update(node*2+1, middle+1, end, idx, diff) # 뒤쪽 절반에서 찾아보는 중

def rangeSum(node, start, end, left, right):        # 노드, 시작, 끝, 합의 시작, 합의 끝
    middle = (start+end)//2                         # 시작과 끝의 중간
    if end<left or right<start:return 0             # 리스트의 범위를 벗어나면 더하면 안되니 0으로 반환
    if left<=start and end<=right:return tree[node] # 리스트의 범위 안에 들어가면 더해야 되니까 값을 반환
    return rangeSum(node*2, start, middle, left, right)+rangeSum(node*2+1, middle+1, end, left, right) # 반환된 값을 더함


if __name__=='__main__':
    l = [None, 6, 7, 2, 5, 10]     # 인덱스 1부터 5까지 있는 리스트
    tree = [0]*10                  # 정점의 합을 기록할 트리를 만들어줌

    init(1, 1, 5)                  # node:1을 시작으로 리스트 1부터 5까지 합을 만들어줌
    update(1, 1, 5, 3, 3)          # node:1을 시작으로 리스트 1부터 5까지 중에서 인덱스 3을 3만큼 더 해줌
    print(rangeSum(1, 1, 5, 3, 5)) # node:1을 시작으로 리스트 1부터 5까지 3부터 5까지 합을 구함