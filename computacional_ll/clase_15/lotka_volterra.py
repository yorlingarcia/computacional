from matplotlib import pyplot as plt
from runge_kutta import Runge

# solucion numerica de la ecuacion de lotja-volterra
# utilizando el metodo de runge-kutta de cuarto orden

# el sistema de ecuaciones es
# dx/dt = alpha*x-beta*x*y apha,beta = constantes
# dy/dt = gamma*x*y-delta*y gamma,delta = constantes

# este sistema respresenta un modelo particular entre dos poblaciones
# donde x representa las presas, x los depredadores, las constantes
# los parametro de mortalidad y crecimiento poblacional
a = 1 #aplha
b = 0.5 #beta
c = 0.5 #gamma
d = 2 #delta
# realizando el cambio de variables para utilizar el metodo de runge-kutta
# de la clase Runge del metodo rk4N, se tiene
fun = []
fun.append('1*y[0]-0.5*y[0]*y[1]')
fun.append('0.5*y[0]*y[1]-2*y[1]')

ro = [2,2] # condicion inicial
h = 0.1 # tamaño del paso(bin)
tt = [0,30] # intervalo temporal

ode = Runge()
(t,r) = ode.rk4N(h,tt,ro,fun)
x = []
y = []
for i in r:
    x.append(i[0])
    y.append(i[1])
#plt.plot(t,r)
plt.plot(t,x,label = 'presas')
plt.plot(t,y,label = 'depredadores')
plt.legend()
plt.show()

