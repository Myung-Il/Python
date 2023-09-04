LA = list(input().upper())
a = list(set(LA))
cnt = [LA.count(i) for i in a]

res = 'a'
MX = -1

for i in range(len(a)):

    if cnt[i] > MX :
        MX = cnt[i]
        res = a[i]
        
    elif cnt[i] == MX :
        res = '?'

print(res)