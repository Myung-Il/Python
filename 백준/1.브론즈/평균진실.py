n = int(input())

for z in range(n):
    a = list(map(int,input().split()))

    n=a[0]
    a=a[1:]

    c=0
    avr = sum(a)/len(a)
    for i in a:
        if i>avr:
            c+=1
    print(f'{(c/n)*100:.3f}%')