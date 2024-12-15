from 나나 import words
import random as r
import time as t
from string import ascii_letters
from re import sub
at = ascii_letters + " []'-"

l = []
for line in words.split('\n'):
    if not line:continue
    part, pin = ['', ''], 0
    for elm in line:
        if elm not in at:pin = 1
        match pin:
            case 0:part[0]+=elm
            case 1:part[1]+=elm
    part[0] = part[0].strip()
    part[1] = part[1].strip()
    l.append(part)

r.shuffle(l)

total, ans, x, count = 0, 0, 1, 0
while x:
    x, c, to = [], 0, 0
    for elm in l:
        total += 1
        to += 1
        s = input(f"{elm[0]} : ")
        if sub(r"\s+", "", s)==sub(r"\s+", "", elm[1]):print('O');ans+=1
        else:
            print(f"X : {elm[1]}")
            c += 1
            x.append(elm)

        print(f"\n남은 문제 수 : {to}/{len(l)},   정답률 : {ans}/{total} : {ans/total*100:.2f}%\n")
        t.sleep(1)
    
    print(f"오답 정리 횟수 : {count},   틀린 횟수 : {c}")
    r.shuffle(x)
    l, count = x, count+1