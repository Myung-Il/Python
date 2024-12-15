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

total, c = 0, 0
for elm in l:
    total += 1
    ty = r.choice(['E', 'K'])
    if ty=="E":
        s = input(f"{elm[0]} : ")
        if sub(r"\s+", "", s)==sub(r"\s+", "", elm[1]):print('O');c+=1
        else:print(f"X : {elm[1]}")
        
    if ty=="K":
        s = input(f"{elm[1]} : ")
        if sub(r"\s+", "", s)==sub(r"\s+", "", elm[0]):print('O');c+=1
        else:print(f"X : {elm[0]}")

    print(f"\n정답률 : {c}/{total} : {c/total*100:.2f}%\n")
    t.sleep(1)