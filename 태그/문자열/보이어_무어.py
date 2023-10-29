def boyer_moore(pattern, text):
    M = len(pattern)
    N = len(text)
    i = 0

    while i <= N-M:
        j = M-1
        while j >= 0:
            if pattern[j] != text[i+j]:
               move = find(pattern, text[i + M - 1])
               break
            j = j - 1
        if j == -1:
            return i
        else:
            i += move
    return -1
 
def find(pattern, char):
    for i in range(len(pattern)-2,-1,-1):
        if pattern[i] == char:
            return len(pattern)-i-1
    return len(pattern)

print(boyer_moore('ABC','ACBABCABCC'))
print(*'ACBABCABCC')
print(*[i for i in range(10)])