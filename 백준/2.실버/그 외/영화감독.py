n = int(input())
i = 0
a = 666

while 1:
    b= list(str(a))

    if b.count('6') >= 3:
        for j in range(len(b)-2):
            if b[j] == b[j+1] == b[j+2] == '6':
                i+=1
                break
    if i == n:
        print(a)
        break
    a+=1