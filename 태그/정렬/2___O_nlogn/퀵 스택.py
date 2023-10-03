l=[4,6,9,12,2,8,11,7,1,3,10,5]

stack = []
stack.append((0, len(l)-1))
while stack:
    start,end = stack.pop()

    pivot_index = (start+end)//2
    pivot = l[pivot_index]

    left,right = start,end
    while left <= right:
        while l[left] < pivot:
            left += 1
        while l[right] > pivot:
            right -= 1
        if left <= right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    if start < right:
        stack.append((start, right))
    if left < end:
        stack.append((left, end))

    print(l)