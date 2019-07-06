from numpy import array, sqrt, linspace
from scipy.integrate import odeint
from matplotlib import pyplot as plt


# sistema de ecuaciones
def df_dt(y, t, G, M, l):
    a = sqrt(y[0]**2 +y[2]**2)
    dy1 = y[1]
    dy2 = -(G*M/a**2)*(y[0]/sqrt(a** +(l/2)**2))
    dy3 = y[3]
    dy4 =  -(G*M/a**2)*(y[2]/sqrt(a** +(l/2)**2))

    return array([dy1, dy2, dy3, dy4])

# Parámetros
G = 1 #6.674e-11 #N.m/kg**2
l = 2
M = 10
# Condiciones iniciales
# posicon
xo = 1
yo = 0
#velocidad
vxo = 0
vyo = 1
conds_iniciales = array([xo, vxo, yo, vyo])

# Condiciones para integración
tf = 50
N = 10000
t = linspace(0, tf, N)

solucion = odeint(df_dt, conds_iniciales, t, args=(G, M, l))

plt.plot(solucion[:,0],solucion[:,2])
plt.show()
