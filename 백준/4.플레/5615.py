from sys import stdin
import random
input = lambda:stdin.readline().rstrip()

n = int(input())
l = [int(input())for _ in range(n)]

def isprime(n):
    if n < 2 or not n & 1:
        return False
    if n == 2:
        return True
    def mrtest(b):
        x = pow(b, t, n)
        if x == 1:
            return True
        for i in range(s):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return False
    s = 0
    t = n - 1
    while not t & 1:
        s += 1
        t >>= 1
    for i in range(10):
        b = random.randrange(2, n)
        if not mrtest(b):
            return False
    return True

print("소수"if isprime(1223)else"합성수")
print("소수"if isprime(1224)else"합성수")