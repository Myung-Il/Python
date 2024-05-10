from sys import stdin
input = lambda:stdin.readline().strip()

a = input()
b = input()

l = [[0 for _ in range(len(b)+1)]for _ in range(len(a)+1)]
for i in range(len(a)+1):l[i][0] = i
for i in range(len(b)+1):l[0][i] = i
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        l[i][j] = min(
            l[i-1][j] + 1,
            l[i][j-1] + 1,
            l[i-1][j-1] + (0 if a[i-1]==b[j-1]else 1)
        )
print(l[-1][-1])