a = list(map(int, input().split()))
j = 1

while 1:
    c = 0
    for i in range(5):
        if j%a[i] == 0:
            c = c + 1

    if c >= 3:
        break

    j = j + 1

print(j)