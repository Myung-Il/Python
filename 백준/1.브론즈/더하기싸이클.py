n = int(input())
b = n
i = 0

while 1 :
    i = i + 1
    a = (b%10)*10 + (b//10 + b%10)%10
    if a==n:
        print(i)
        break
    b = a