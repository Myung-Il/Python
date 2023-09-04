a = input()
i = 0

while 1 :
    i+=1
    A = (" ").join(a).split(" ")
    B = int(A[0]) + int(A[1])
    a = str(A[1]) + str(B)
    if a == A:
        break

print(A)
print(B)
print(i)