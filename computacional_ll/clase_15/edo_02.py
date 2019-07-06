from runge_kutta import Runge
from matplotlib import pyplot as plt
from numpy import zeros, array, shape
# solucion de una EDO multivariable(dos variables
# por el metodo de runge kutta, con el cambio de variable

# condiciones iniciales
ro = [1,1]

# intervalo temporal
to = 0
tf = 10
tt = [to,tf]

# paso de los datos
h = 0.1

# funciones de primer orden
# funcion del problema
# dx/dt = x*y-x
# dy/dt = y-x*y+(sin(t))^2

# cambio de variable para llamar a la funcion rk4N
fun = []
fun.append('y[0]*y[1]-y[0]')
fun.append('y[1]-y[0]*y[1]+(sin(t))**2')

#llamar a la clase rk4N
ode = Runge()

# solucion utilizando el metodo ode4vec
(t,r) = ode.rk4N(h,tt,ro,fun)
# grafica de la solucion
plt.plot(t,r)
plt.show()
