n = int(input())

A = 0
B = 1
i = 0

while 1 :
    i = i+1

    T = A + B

    A = B
    B = T
    
    if n==i:
        print(A)
        break





# def gegi(n):
#     if n==0 or n==1:
#         return n
#     return gegi(n-1)+gegi(n-2)
# print(gegi(int(input())))