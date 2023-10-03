l=[4,6,9,12,2,8,11,7,1,3,10,5]

def h(l,left,right):
    r00t = l[left]
    
    parent = left
    while parent<(right+1)//2:
        child_left = parent*2+1
        child_right = child_left+1

        if child_right<=right and l[child_right]>l[child_left]:child = child_right
        else: child = child_left

        if r00t>=l[child]:break

        l[parent] = l[child]
        parent = child
    l[parent] = r00t

    print(l)

n = len(l)
for i in range((n-1)//2,-1,-1):h(l,i,n-1)
for i in range(n-1,0,-1):
    l[0],l[i] = l[i],l[0]
    h(l,0,i-1)