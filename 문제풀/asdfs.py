from sys import stdin
input = lambda:stdin.readline().rstrip()

class SegmentTree:
    def __init__(self, arr, N):
        self.arr = arr
        self.tree = [0]*N*4

    def query(self, node, start, end, rank):
        if start == end:
            return start

        mid = (start + end) // 2
        left = self.tree[node * 2]
        if left >= rank:
            return self.query(node * 2, start, mid, rank)
        return self.query(node * 2 + 1, mid + 1, end, rank - left)

    def update(self, node, start, end, idx, diff):
        if end < idx or idx < start:
            pass
        elif start == end:
            self.tree[node] += diff
        else:
            mid = (start + end) // 2
            temp1 = self.update(node * 2, start, mid, idx, diff)
            temp2 = self.update(node * 2 + 1, mid + 1, end, idx, diff)
            self.tree[node] = temp1 + temp2
        return self.tree[node]


T = int(input())

N = 1_000_000 + 1
tree = SegmentTree([0] * N, N)
answer = []
for _ in range(T):
    q, *n = map(int, input().split())
    if q == 1:
        out = tree.query(1, 1, N, n[0])
        print(out)
        tree.update(1, 1, N, out, -1)
    if q == 2:
        tree.update(1, 1, N, n[0], n[1])