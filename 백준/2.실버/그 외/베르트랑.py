import sys

l = [True]*246914
k = 2

while k < 246914:
    if l[k] == True:
        for i in range(k*2, 246914, k):
            l[i] = False
    k += 1


while 1:
    a = int(sys.stdin.readline().rstrip())
    if a == 0: exit()

    t = 0
    for i in range(a+1, a*2+1):
        if l[i] == True:
            t += 1
    print(t)