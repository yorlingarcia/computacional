# -*- coding: utf-8 -*-
"""
Created on Thu May 23 09:47:29 2019

@author: Yorlin García
"""
import numpy as np
from matplotlib import pyplot as plt

outDisdat = open("../data/falling.txt")
t = []
y = []
for i in outDisdat:
	column = i.split()
	if column[0] != "//Falling" and column[0] != "//Time":
		t.append(float(column[0]))
		y.append(float(column[1]))
plt.figure(1)
plt.plot(t,y,'bo')
# velocidad
Dt = round((max(t)-min(t))/len(y),4)
#print(Dt)
#print(t)
ypos = -1*np.array(y)
v = np.zeros(len(y))
a = np.zeros(len(y))
for i in range(1,len(y)-1):
	v[i] = (ypos[i+1]-ypos[i-1])/(2*Dt)
	a[i] = (ypos[i+1]-2*ypos[i]+ypos[i-1])/(round(Dt**2,4))

#print(v)
#print(a)
plt.figure(2)
plt.plot(t,v,'or',label = 'velocidad')
plt.legend()
plt.figure(3)
plt.plot(t,a,'og', label = 'aceleración')
plt.grid("on")
plt.legend()
plt.figure(4)
plt.plot(v,a,'bo')
plt.grid("on")

outDisdat = open("datafile.dat","w")
for i in range(len(a)):
    outDisdat.write('%0.4f  %0.4f\n' % (t[i] ,a[i]))
outDisdat.close()

##################################
import numpy
import matplotlib.pyplot as plt
from Mincuad import Minimoscuadrados
from scipy import linspace

Dat = numpy.loadtxt("datafile.dat")
D = numpy.copy(Dat) 
print(D)
Mc = Minimoscuadrados()
[a1,a2,sigma] = Mc.min(D)
x = linspace(min(D[:,0]),max(D[:,0]),100)
g = a1 +a2*x
plt.figure(5)
plt.plot(D[:,0],D[:,1],'bo')
plt.plot(x,g,'b--')
plt.title('Interpolación minimos cuadrados')
plt.ylabel('Numero de particulas Ln(N)')
plt.xlabel('Tiempo')
plt.legend(('interpolación','Linealizacion de los datos'),loc='upper right')
#plt.text(60, 2.7, r'$ \tau $ = %0.4f'%(1/(a2*(-1))), fontsize=10)
