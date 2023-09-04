from sys import stdin as st

n=1000000
s=[False,False]+[True]*(n-1)
for i in range(2,n+1):
    if s[i]==True:
        for j in range(i*2,n+1,i):
            s[j]=False

while 1:
    z=int(st.readline().rstrip())
    
    if z==0:break

    if z%2!=0:
        print("Goldbach's conjecture is wrong.")
    else:
        for i in range(3,z//2+1,2):
            if s[i]and s[z-i]:
                print(f'{z} = {i} + {z-i}')
                break