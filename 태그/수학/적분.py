import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (1/((2*np.pi)**0.5))*np.exp(-(x**2)/2)

x=[i/100 for i in range(300)]
y=[f(i) for i in x]

yf=sum([y[i]*0.01 for i in range(300)])

print(yf)