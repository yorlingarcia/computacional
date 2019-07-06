# -*- coding: utf-8 -*-
"""
Created on Wed May 22 22:17:31 2019

@author: Yorlin García
"""

from Euler import Euler
from scipy import linspace
from matplotlib import pyplot as plt
import numpy as np

fun = '2*a*b'

h = 0.05
xo = 1
yo = 1
Xmin = 1
Xmax = 1.5

Eu= Euler()
[t,y] = Eu.normal(xo,yo,Xmin,Xmax,h,fun)
plt.plot(t,y)
[x,Y] = Eu.mejorado(xo,yo,Xmin,Xmax,h,fun)
plt.plot(x,Y)
z1 = linspace(Xmin,Xmax,int((Xmax-Xmin)/h))
z2 = np.exp(z1**2 -1)
plt.plot(z1,z2)