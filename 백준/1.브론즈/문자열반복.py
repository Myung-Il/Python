n = int(input())
i=0

while i<n:
    k,a = input().split()
    s = ""

    for j in a:
        s+=j*int(k)

    i+=1
    print(s)        