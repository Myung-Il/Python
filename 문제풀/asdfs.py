import heapq as hq
from sys import stdin
input = lambda:stdin.readline().rstrip()


n,k = map(int,input().split())
l = []
for i in range(k):
    fst,sec = map(int,input().split())
    l.append([fst,sec])