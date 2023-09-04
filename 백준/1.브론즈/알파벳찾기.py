# K = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

abc = list(input())

K = [-1] * 26


for i in range(len(abc)-1, -1, -1):
    K[ord(abc[i])-97] = i


print(*K)