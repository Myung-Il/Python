from collections import Counter
import sys # sys.stdin.readline().rstrip()

n = int(sys.stdin.readline().rstrip())
l = []

Arithmetic_mean = 0 # 산술 평균
Median_value = 0 # 중앙값
The_lowes_price = 0 # 최빈값
Range = 0 # 범위

for i in range(n):
    a = int(sys.stdin.readline().rstrip())
    l.append(a)

Arithmetic_mean = round(sum(l)/n) # 산술 평균


l.sort()
if int(len(l)/2)%2 == 0:
    Median_value = l[round(len(l)/2)] # 중앙값
else:
    Median_value = l[round(len(l)/2)-1] # 중앙값


co = 0
oo = Counter(l)
ooo = []
for v in oo:
    if oo[v] == max(oo.values()):
        ooo.append(v)
    
ooo = sorted(list(ooo))
if len(ooo) > 1:
    The_lowes_price = ooo[1] # 최빈값
else:
    The_lowes_price = ooo[0] # 최빈값


Range = abs(max(l)-min(l)) # 범위

print(Arithmetic_mean)
print(Median_value)
print(The_lowes_price)
print(Range)