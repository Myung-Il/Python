from datetime import timedelta as td
from time import time, sleep

l = []
for _ in range(1000):
    start = time()
    ##############
    
    import random
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
    
    ############
    end = time()
    l.append(td(seconds=end - start))

average_time = sum(l, td()) / 1000
print(average_time)
