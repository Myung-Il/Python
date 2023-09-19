chang = sang = 100
n = int(input())
for i in range(n):
    num1, num2 = map(int, input().split())
    
    if num1 > num2:
        sang -= num1
    else:
        chang -= num2

print(chang)
print(sang)