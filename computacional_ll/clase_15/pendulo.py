from runge_kutta import Runge
import numpy as np
from matplotlib import pyplot as plt
from vpython import *
from math import *


g = 9.8
l = 0.1
# realizando el cambio de variables para utilizar el metodo de runge-kutta
# de la clase Runge del metodo rk4N, se tiene
fun = []
fun.append('y[1]')
fun.append('-(9.8/0.1)*sin(y[0])')
theta_ini = 179*(np.pi/180)
theta_pto_ini = 0
ro = [theta_ini, theta_pto_ini] # condicion inicial
h = 0.1 # tamaño del paso(bin)
tt = [0,10] # intervalo temporal

ode = Runge()
(t,r) = ode.rk4N(h,tt,ro,fun)
theta =np.zeros(len(t))
theta_pto = np.zeros(len(t))
j = 0
for i in r:
    theta[j] = i[0]
    theta_pto[j] = i[1]
    j += 1
print(theta)

x = l*np.sin(theta)
y = -l*np.cos(theta)
xo = l*np.sin(theta_ini)
yo = -l*np.cos(theta_ini)
plt.plot(x,y)
plt.show()
p = sphere( pos = vector (xo,yo,0), radius = 0.01, color =  color.cyan, make_trail = True, trail_type = 'points', iterval = 10, retain = 50)
p2 = cylinder(pos = vector(0,0,0), axis = vector(xo,yo,0),radius = 0.005)
for i  in range(len(t)):
    rate(1)
    p2.axis = vector(x[i],y[i],0)
    p.pos = vector(x[i],y[i],0)


