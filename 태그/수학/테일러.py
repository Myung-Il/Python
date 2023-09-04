import numpy as np
import matplotlib.pyplot as plt

def fact(n):
    res = 1
    for i in range(1, n+1):
        res*=i
    return res

def sinxxx(x):
    res = 0
    n = 10
    while n>=0:
        res += ((-1)**n)*((x**(2*n+1))/fact(2*n+1))
        n -= 1
    return res

print(sinxxx(1))
print(np.sin(1))


x=[i/100 for i in range(1000)]
y=[np.sin(i) for i in x]

x1=[i/100 for i in range(1000)]
y1=[sinxxx(i) for i in x]

p=[0 for i in x]

plt.plot(x1,y1)
plt.plot(x,y)
plt.plot(x,p)
plt.show()