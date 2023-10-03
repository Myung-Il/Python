l=[4,6,9,12,2,8,11,7,1,3,10,5]

def qwe(l):
    n=len(l)
    if n <= 1:
        return
    mid=n//2
    lt = l[:mid]
    rt = l[mid:]

    qwe(lt)
    qwe(rt)

    i,j,p=0,0,0
    
    print('=======',lt,rt)
    while i<len(lt) and j<len(rt):
        if lt[i] < rt[j]:
            l[p]=lt[i]
            i+=1
            p+=1
        else:
            l[p]=rt[j]
            j+=1
            p+=1
    while i<len(lt):
        l[p]=lt[i]
        i+=1
        p+=1
    while i<len(rt):
        l[p]=rt[j]
        j+=1
        p+=1

qwe(l)
print(l)