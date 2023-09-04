n = int(input())
p, total=0, 0

for j in range(n):
    a = list(map(str,input().split()))
    b = " ".join(a)
        
    for i in b:
        if i == 'O':
            p+=1
            total += p
        else:
            p=0
    print(total)
    p, total=0, 0


# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOXq