from collections import deque
from sys import stdin
input = lambda:stdin.readline().rstrip()


if __name__=='__main__':
    n = int(input())
    q = deque(map(int,input().split()))

    stk = []
    los = 1
    while 1:
        elm = q.popleft()
        if elm==los:los+=1
        elif stk and stk[-1]:
            