a,b=map(int,input().split())

def f(n,s):
    c=0
    while n:
        n//=s
        c+=n
    return c

print(min(f(a,5)-f(b,5)-f(a-b,5),f(a,2)-f(b,2)-f(a-b,2)))


'''
25 12 --- 2
5200300
5200300

65 40 --- 0
651687674221131912
651687674221131904

65 41 --- 2
397370533061665800
397370533061665792
'''