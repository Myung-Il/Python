l = [4,6,9,12,2,8,11,7,1,3,10,5]

n = len(l)
z = n//2
while z>0:
    for i in range(z,n):
        j = i-z
        t = l[i]
        while j>=0 and l[j]>t:
            l[j+z] = l[j]
            j -= z
        l[j+z] = t
    z //= 2
    print(l)