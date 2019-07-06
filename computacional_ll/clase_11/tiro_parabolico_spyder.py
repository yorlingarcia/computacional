# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 21:37:28 2019

@author: Yorlin García
"""
from matplotlib import pyplot as plt
import numpy as np
from scipy import linspace
# para que theta x es xmax
# ecuaciones tiro parabolico
# m(dvx/dt) = -c sqrt(vx2+vy2)vx
# m(dvy/dt) = -c sqrt(vx2+vy2)vy -mg
def euler(g,Vo,Yo,tmin,tmax,Deltat,fun):
    N = (tmax - tmin)/Deltat
    t = linspace(tmin,tmax,int(N))
    v = np.zeros(len(t))
    y = np.zeros(len(t))
    y[0] = Yo
    v[0] = Vo
    for i in range(len(t)-1):
        V = v[i]
        acel = float(eval(fun))
        v[i+1] = v[i] + Deltat*acel
        y[i+1] = y[i] + Deltat*v[i]
    return(t,y,v)
	
g = 9.8 #m/s2
Vo = 10.8 #m/s
m = 1 #kg
Xo = 0
Yo = 2
tmin = 0
tmax = 2.4
N = 300
Deltat = (tmax-tmin)/N
#funx = '-c*np.sqrt(vx**2+vy**2)*vx'
#funy = '-c*np.sqrt(vx**2+vy**2)*vy-m*g'
# fd = 0
funx = '0'
funy = '-g'


aux2 = 0 # maximo x
aux3 = 0 # guarda el angulo
angulo = []
distmax = []
for i in range(90+1):
	theta = i*(np.pi/180)
	angulo.append(theta*180/np.pi)
	Vx = Vo*np.cos(theta)
	Vy = Vo*np.sin(theta)
	(t,x,vx)=euler(g,Vx,Xo,tmin,tmax,Deltat,funx)
	(t,y,vy)=euler(g,Vy,Yo,tmin,tmax,Deltat,funy)
	aux1 = 0 #cambio de signo en y
	for j in range(len(y)):
		if aux1 > y[j]:
			aux1 = j-1
			xmax = x[aux1]
			#print(i,aux1)
			distmax.append(xmax)
			aux1 = 0
			if aux2 < xmax:
				aux2 = xmax
				aux3 = theta*180/np.pi
				break
			break
    
print('distancia maxima: %f, theta: %f°' % (aux2,aux3))
plt.plot(angulo, distmax)