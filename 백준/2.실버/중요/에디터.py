from sys import stdin as st

s1=list(st.readline().rstrip())
s2=[]
for i in range(int(st.readline())):
    a=st.readline().rstrip()
    if a=='L':
        if len(s1)>0:s2.append(s1.pop())
    elif a=='D':
        if len(s2)>0:s1.append(s2.pop())
    elif a=='B':
        if len(s1)>0:s1.pop()
    elif a[0]=='P':
        s1.append(a[-1])

print(''.join(s1+s2[::-1]))