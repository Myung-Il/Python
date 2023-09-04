from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    a, b = map(int,sys.stdin.readline().rstrip().split())
    m = list(map(int,sys.stdin.readline().rstrip().split()))
    k = deque(m)
    ko = deque(j for j in range(len(k)))
    c = 0

    while 1:
        if k[0] == max(k):
            k.popleft()
            c+=1
            if ko[0] == b:
                print(c)
                break
            ko.popleft()

        else:
            k.append(k.popleft())
            ko.append(ko.popleft())