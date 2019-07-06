from matplotlib import pyplot as plt
import numpy as np
from scipy import linspace
from vpython import *

def euler(g,Cd,Cm,Vox,Voy,Voz,Wx,Wy,Wz,Xo,Yo,Zo,tmin,tmax,Deltat,funx,funy,funz):

    N = (tmax - tmin)/Deltat
    t = linspace(tmin,tmax,int(N))

    vx = np.zeros(len(t))
    vy = np.zeros(len(t))
    vz = np.zeros(len(t))

    x = np.zeros(len(t))
    y = np.zeros(len(t))
    z = np.zeros(len(t))

    x[0] = Xo
    y[0] = Yo
    z[0] = Zo

    vx[0] = Vox
    vy[0] = Voy
    vz[0] = Voz

    for i in range(len(t)-1):

        Vx = vx[i]
        Vy = vy[i]
        Vz = vz[i]

        acel1 = float(eval(funx))
        acel2 = float(eval(funy))
        acel3 = float(eval(funz))

        vx[i+1] = vx[i] + Deltat*acel1
        vy[i+1] = vy[i] + Deltat*acel2
        vz[i+1] = vz[i] + Deltat*acel3

        x[i+1] = x[i] + Deltat*vx[i]
        y[i+1] = y[i] + Deltat*vy[i]
        z[i+1] = z[i] + Deltat*vz[i]

    return(t,x,y,z)

g = 9.8 # m/S2
M = 0.149 #kg
Cd = 0
Cm = 0

Vo = 5
alpha = 0*np.pi/180
beta = 90*np.pi/180
gamma = 90*np.pi/180
Vx = Vo*np.cos(alpha)
Vy = Vo*np.cos(beta)
Vz = Vo*np.cos(gamma)
##########################
wo = 200
alphaw = 90*np.pi/180
betaw = 0*np.pi/180
gammaw = 90*np.pi/180
Wx = wo*np.cos(alphaw)
Wy = wo*np.cos(betaw)
Wz = wo*np.cos(gammaw)
##########################
Xo = 0
Yo = 0
Zo = 0

tmin = 0
tmax = 2*Vo/g
N = 300
Deltat = (tmax-tmin)/N

funx = '-Cd*((Vx**2+Vy**2+Vz**2)**0.5)*Vx+Cm*(Wy*Vz-Wz*Vy)'
funy = '-Cd*((Vx**2+Vy**2+Vz**2)**0.5)*Vy+Cm*(Wz*Vx-Wx*Vz)'
funz = '-g-Cd*((Vx**2+Vy**2+Vz**2)**0.5)*Vz+Cm*(Wx*Vy-Wy*Vx)'

(t,x,y,z) = euler(g,Cd,Cm,Vx,Vy,Vz,Wx,Wy,Wz,Xo,Yo,Zo,tmin,tmax,Deltat,funx,funy,funz)

arrow_x = arrow(pos = vector(0,0,0), axis = vector(0.5,0,0), color = color.red)
arrow_y = arrow(pos = vector(0,0,0), axis = vector(0,0.5,0), color = color.green)
arrow_z = arrow(pos = vector(0,0,0), axis = vector(0,0,0.5), color = color.blue)

#scene.range = 4
#scene.forward = vector(0,0,0)
R = 0.2
p = sphere(pos = vector(Xo,Yo,Zo) ,radius = R, color = color.cyan, make_trail=True, trail_type='points', interval=10, retain=50)
for i in range(len(t)):
    rate(30)
    p.pos = vector(x[i],y[i],z[i])

