# -*- coding: utf-8 -*-
"""
Created on Wed May 22 23:46:51 2019

@author: Yorlin García
"""

from EulerSegundo import EulerSegundo
from matplotlib import pyplot as plt
from numpy import sin,pi,sqrt,cos
#from IPython import display
#import time


k =1
m = 1

fun = '-a' # m y k = 1 -(k/m)x

Vo = 0
Xo = 1
tmin = 0
tmax = 20
Deltat = 0.05
plt.figure(1)
Eu= EulerSegundo()
[t,x] = Eu.normal(Vo,Xo,tmin,tmax,Deltat,fun)
plt.plot(t,x)
[t2,x2] = Eu.mejorado(Vo,Xo,tmin,tmax,Deltat,fun)
plt.plot(t2,x2)
A = 1
phi = pi/2
w = sqrt(k/m)
y = A*sin(w*t+phi)
plt.plot(t,y)

plt.legend(('Euler_normal', 'Euler_mejorado','Anlitica'),
prop = {'size':10}, loc = 'upper right')