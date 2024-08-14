def mult(p, q, mod):
    p %= mod
    q %= mod
    r, w = 0, p
    while q:
        if q%2:r = (r+w)%mod
        w = (2*w)%mod
        q >>= 1
    return r

def pow_mod(a, m, p):
    ret = 1
    a %= p

    while m:
        if m%2:ret = mult(ret, a, p)
        a = mult(a, a, p)
        m >>= 1
    return ret

def millerRabin(n, a):
    k = n-1
    while 1:
        d = pow_mod(a, k, n)
        if k%2:return (d==1 or d==n-1)
        if d==n-1:return True
        k >>= 1

def isPrime(n):
    if n==1:return False

    for elm in prime:
        if n==elm:return True
        if n%elm==0:return False
        if not millerRabin(n, elm):return False
    return True
        


if __name__=="__main__":
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    
    print("소수"if isPrime(1223)else"합성수")
    print("소수"if isPrime(1224)else"합성수")