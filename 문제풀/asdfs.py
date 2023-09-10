nova,orgin=map(int,input().split())

nova_u=list(map(int,input().split()))
orgin_u=list(map(int,input().split()))

n_cnt,o_cnt=0,0

n=0
s=0
for i in nova_u:
    if s>n:
        n+=100
        n_cnt+=1
    s+=i

o=0
s=0
for i in orgin_u:
    if s>o:
        o+=360
        o_cnt+=1
    s+=i

print(n_cnt,o_cnt)