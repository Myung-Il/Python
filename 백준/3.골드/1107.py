n,m=map(int,input().split())
l=[]
tf=[]
for i in range(n):
    l.append(list(map(int,input().split())))
    tf.append([False]*m)
mx=0

X=[1,-1,0,0]
Y=[0,0,1,-1]
def other(x,y,t,c):
    global mx
    if c==4:
        mx=max(t,mx)
        return
    for i in range(4):
        xn=x+X[i]
        yn=y+Y[i]
        if xn<0 or xn>=m or yn<0 or yn>=n or tf[yn][xn]:
            continue
        tf[yn][xn]=True
        other(xn,yn,t+l[yn][xn],c+1)
        tf[yn][xn]=False

def the(x,y):
    arr=[]
    for i in range(4):
        xn=x+X[i]
        yn=y+Y[i]
        if xn<0 or xn>=m or yn<0 or yn>=n:
            continue
        arr.append(l[yn][xn])
    ln=len(arr)
    if ln==4:
        arr.sort(reverse = True)
        arr.pop()
    return max(sum(arr)+l[y][x],mx)

for i in range(n):
    for j in range(m):
        tf[i][j]=True
        other(j,i,l[i][j],1)
        tf[i][j]=False
        mx=max(the(j,i), mx)

print(mx)