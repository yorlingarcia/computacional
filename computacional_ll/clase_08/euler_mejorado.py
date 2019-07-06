# -*- coding: utf-8 -*-
"""
Created on Tue May 21 18:53:54 2019

@author: Yorlin García
"""
import numpy as np
from scipy import linspace
from matplotlib import pyplot as plt

Deltax = 0.1
xo = 1.
yo = 1.
Xmin = 1
Xmax = 1.5

h = 0.1
N = (Xmax -Xmin)/h
y = np.zeros(int(N))
u = np.zeros(int(N))
y[0] = yo
u[0] = yo

x = linspace(Xmin,Xmax,N)
fun = '2*a*b'

def Funcion(x1,y1,fun):
	a = x1
	b = y1
	Ecu = eval(fun)
	return(Ecu)
	
for i in range(int(N)-1):
	u[i+1] = y[i]+Deltax*Funcion(x[i],y[i],fun)
	y[i+1] = y[i]+Deltax*(0.5)*( Funcion(x[i],y[i],fun) + Funcion(x[i+1],u[i+1],fun) )

Y = np.exp(x**2 -1)
plt.plot(x,y)
plt.plot(x,Y)
plt.legend(('Euler', 'Analitica'),
prop = {'size':10}, loc = 'upper right')
#plt.plot(x,z)
#plt.legend(('Euler h = 0.1', 'Analitica','Euler h = 0.05'),
#prop = {'size':10}, loc = 'upper right')