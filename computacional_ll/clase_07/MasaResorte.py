#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 19:43:22 2019

@author: usuario
"""

import numpy as np
from scipy import linspace
from matplotlib import pyplot as plt
from numpy import sin,pi,sqrt

m = 1
k = 1

Vo = 0
Xo = 1
tmin = 0
tmax = 20
Deltat = 0.05
N = (tmax - tmin)/Deltat +1
t = linspace(tmin,tmax,N)

v = np.zeros(len(t))
x = np.zeros(len(t))
x[0] = Xo
v[0] = Vo

def acel(x):
    a = -(k/m)*x
    return(a)

for i in range(len(t)-1):
    v[i+1] = v[i] + Deltat*acel(x[i])
    x[i+1] = x[i] + Deltat*v[i]

a = 1
phi = pi/2
w = sqrt(k/m)
y = a*sin(w*t+phi)

er = abs(1-x/y)*100
plt.subplot(2,1,1)
plt.plot(t,x)
plt.plot(t,y)
plt.legend(('Euler', 'Analitica'),
prop = {'size':10}, loc = 'upper right')
plt.subplot(2,1,2)
plt.plot(t,er)