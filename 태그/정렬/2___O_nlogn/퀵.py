l=[4,6,9,12,2,8,11,7,1,3,10,5]

def q(l,left,right):
    x = l[(left+right)//2]

    le = left
    ri = right
    while le<=ri:
        while l[le]<x: le += 1
        while l[ri]>x: ri -= 1

        if le<=ri:
            l[le],l[ri] = l[ri],l[le]
            le += 1
            ri -= 1
    print(l,f'--- 정렬 구간 : {l[left:right+1]}')
    
    if left<ri: q(l,left,ri)
    if le<right:q(l,le,right)

q(l,0,len(l)-1)