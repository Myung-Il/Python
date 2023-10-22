seg = [0 for _ in range(4040404)]
lazy = [0 for _ in range(4040404)]
 
def updateLazy(x, s, e):
    if lazy[x]:
        seg[x] += (e - s + 1) * lazy[x]
        if s != e:
            lazy[x * 2] += lazy[x]
            lazy[x * 2 + 1] += lazy[x]
        lazy[x] = 0
 
 
def update(x, l, r, s, e, dif):
    updateLazy(x, s, e)
    if e < l or r < s:
        return
    if l <= s and e <= r:
        seg[x] += (e - s + 1) * dif
        if s != e:
            lazy[x * 2] += dif
            lazy[x * 2 + 1] += dif
        return
    m = s + e >> 1
    update(x * 2, l, r, s, m, dif)
    update(x * 2 + 1, l, r, m + 1, e, dif)
    seg[x] = seg[x * 2] + seg[x * 2 + 1]
 
def getSum(x, l, r, s, e):
    updateLazy(x, s, e)
    if e < l or r < s:
        return 0
    if l <= s and e <= r:
        return seg[x]
    m = s + e >> 1
    return getSum(x * 2, l, r, s, m) + getSum(x * 2 + 1, l, r, m + 1, e)