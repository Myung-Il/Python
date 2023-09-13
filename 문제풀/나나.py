n = int(input())
k = int(input())

start = 1
end = k
r = 0
while start <= end :
    m = (start + end) // 2
    t = 0

    for i in range(1, n+1) :
        t += min(m // i, n)

    if t < k :
        start = m + 1
    elif t >= k :
        r = m
        end = m - 1

    print(start,end,'===',m,t,r)

print(r)