import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (1/((2*np.pi)**0.5))*np.exp(-(x**2)/2)

x=[i/100 for i in range(300)]
y=[f(i) for i in x]

h=0.001
yp=[(f(i+h)-f(i-h))/(2*h) for i in x]

o=[0 for i in x]

plt.plot(x,y)
plt.plot(x,o)
plt.plot(x,yp)
plt.show()