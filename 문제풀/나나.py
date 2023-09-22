s=input()
l=[]

r=len(s)
for i in range(1,r-1):
    for j in range(i+1,r):
        find=s[:i][::-1]+s[i:j][::-1]+s[j:][::-1]
        l.append(find)

print(sorted(l)[0])