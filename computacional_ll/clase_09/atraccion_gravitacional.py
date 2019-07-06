# -*- coding: utf-8 -*-
"""
Created on Thu May 23 07:24:48 2019

@author: Yorlin García
"""

import numpy as np
from scipy import linspace
from matplotlib import pyplot as plt

Deltat = 0.001
xo = 100
Vo = 0
tmin = 0
tmax = 6
M = 5.92e24
N = (tmax -tmin)/Deltat
x = np.zeros(int(N))
u = np.zeros(int(N))
v = np.zeros(int(N))
x[0] = xo
u[0] = xo
v[0] =Vo
t = linspace(tmin,tmax,int(N))
fun = '-((6.67e-11)*5.92e24)/(6.37e6 + a)**2'
R = np.zeros(int(N))+ 6.37e6
def Funcion(x1,fun):
	a = 0.
	a = x1
	Ecu = eval(fun)
	return(Ecu)
tc = 0
for i in range(int(N)-1):
	v[i+1] = v[i] + Deltat*(Funcion(x[i],fun))
	u[i+1] = v[i]+Deltat*Funcion(x[i],fun)
	x[i+1] = x[i]+Deltat*(0.5)*(v[i]+u[i+1])
	if x[i+1]<=0:
		tc = i
		break
print(x[tc],-v[tc],tc*Deltat)
print(-v[tc]+v[tc]*0.01)

plt.figure(1)	
plt.plot(t[0:tc],(x[0:tc]+6.37e6 ))
plt.plot(t,R)
plt.legend(('posición de la particula', 'Radio de la tierra'),
prop = {'size':10}, loc = 'upper right')
#plt.plot(t[tc],(x[tc]+6.37*10**6 ),'or')
plt.figure(2)
plt.plot(t[0:tc],v[0:tc])
plt.legend(('velocidad'),
prop = {'size':10}, loc = 'upper right')
#plt.ylim([-1,max(x)+6.37*10**6])