from sys import stdin as st
import string

l=list(st.readline().rstrip())
st=[]
an=''
for i in l:
    if i in string.ascii_uppercase:
        an+=i

    elif i=='(':
        st.append(i)
    
    elif i=='*'or i=='/':
        while st and (st[-1]=='*'or st[-1]=='/'):
            an+=st.pop()
        st.append(i)
        
    
    elif i=='+'or i=='-':
        while st and st[-1]!='(':
            an+=st.pop()
        st.append(i)

    
    else:
        while st and st[-1]!='(':
            an+=st.pop()
        st.pop()

while st:
    a=st.pop()
    if a!='(':an+=a

print(an)



'''
A*(B+C) ---- ABC+*
A+B ---- AB+
A+B*C ---- ABC*+
A+B*C-D/E ---- ABC*+DE/-

G*(A-B*(C/D+E)/F) --- GABCD/E+*F/-*
A+B+C*D-E*F ---- AB+CD*+EF*-
(A+((B+C*D)+E)) ---- ABCD*+E++
'''