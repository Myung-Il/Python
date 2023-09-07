import random as r

r_n1,r_n2,r_n3=r.randrange(1,10),r.randrange(1,10),r.randrange(1,10)
cnt=0

r_l=[r_n1,r_n2,r_n3]
while 1:
    n1,n2,n3=map(int,input('숫자 3개 입력 : ').split())
    n_l=[n1,n2,n3]
    cnt+=1

    s,b,o=0,0,0
    for i in n_l:
        if i in r_l:
            if n_l.index(i)==r_l.index(i):
                s+=1
                continue
            b+=1
            continue
        o+=1
        continue
    print(s,b,o)

    if s==3:
        break

print('게임이 종료되었습니다')