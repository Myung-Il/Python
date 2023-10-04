def po(l1,l2):
    ls = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for h in range(2):
                ls[i][j] += l1[i][h]*l2[h][j]
            ls[i][j] %= 1_000_000_007
    return ls

def dac(li,u):
    if u==1:return li
    else:
        x = dac(li,u//2)
        if u%2==0:return po(x,x)
        else:return po(po(x,x),li)


if __name__=='__main__':
    n = int(input())
    l = [[1,1],[1,0]]
    ans = dac(l,n)[0][1]
    print(ans%1_000_000_007)