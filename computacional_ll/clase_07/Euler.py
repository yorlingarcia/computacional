#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:24:00 2019

@author: usuario
"""

import numpy as np
from scipy import linspace
from matplotlib import pyplot as plt

Deltax = 0.1
Xo = 1
Yo = 1
Xmin = 1
Xmax = 1.5

h = 0.1
N = (Xmax -Xmin)/h
y = []
y.append(Yo)
x = linspace(Xmin,Xmax,N)
def Funcion(x,y):
    Ecu = 2*x*y
    return(Ecu)

for i in range(len(x)-1):
    y.append(Yo +h*Funcion(Xo,Yo))
    Yo = y[i+1]
    Xo = Xo+h
    

Y = np.exp(x**2 -1)
plt.plot(x,y)
plt.plot(x,Y)

h = 0.05
N = (Xmax -Xmin)/h
z = []
Yo = 1
z.append(Yo)
x = linspace(Xmin,Xmax,N)
Xo = 1
for i in range(len(x)-1):
    z.append(Yo+h*Funcion(Xo,Yo))
    Yo = z[i+1]
    Xo = Xo+h

plt.plot(x,z)
plt.legend(('Euler h = 0.1', 'Analitica','Euler h = 0.05'),
prop = {'size':10}, loc = 'upper right')