l=[3,9,12,1,5,8,7,6]

def qwe(l):
    n=l[-1]
    
    print('-=-=-=-',l)

    sl=list()
    ll=list()
    for i in l:
        if i==n:
            l=sl+[n]+ll
        elif i < n:
            sl.append(i)
        else:ll.append(i)


    sl = qwe(l[:l.index(n)])
    ll = qwe(l[l.index(n)+1:])


    print(sl,ll,'=====',l)


print(qwe(l))