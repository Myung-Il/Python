l=[4,6,9,12,2,8,11,7,1,3,10,5]

def qwe(l):
    n=len(l)
    if n <= 1:
        return
    middle=n//2
    left = l[:middle]
    right = l[middle:]

    qwe(left)
    qwe(right)

    i,j,p=0,0,0
    
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            l[p]=left[i]
            i+=1
            p+=1
        else:
            l[p]=right[j]
            j+=1
            p+=1

    while i<len(left):
        l[p]=left[i]
        i+=1
        p+=1
        
    while j<len(right):
        l[p]=right[j]
        j+=1
        p+=1
    print(l,f'--- 정렬 부분 left : {left} /// right : {right}')

qwe(l)