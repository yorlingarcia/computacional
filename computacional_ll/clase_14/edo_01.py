from runge_kutta import Runge
from matplotlib import pyplot as plt
# solucion de una ecuacion diferencial de una sola variable dependiente
# utilizando el metodo de runge-kutta de cuarto orden

# condiciones iniciales
# teniendo en cuenta el cambio de variable t = U/(U-1)
# para un tiempo infinito en el rango de u en [0,1]

to = 0 # tiempo inicial
ro = [1] # posicion inicial " tener en cuenta que es una array
h = 0.1 # cantidad de datos

fun = []
fun.append('1/(y[0]**2*(1-u)**2+u**2)') # funcion de primer orden " debe ser una lista"
# se llama la clase
ode = Runge()
(u,r) = ode.rk4NU(h,to,ro,fun) #metodo de la clase para el cambio de variable en t
t = u/(1-u) # revertiendo el cambio de variable
plt.plot(t,r) # grafica de la solucion
plt.xlabel('t')
plt.ylabel('x')
plt.show()
