import numpy
import matplotlib.pyplot as plt
from Mincuad import Minimoscuadrados
from scipy import linspace

Dat = numpy.loadtxt("data.dat")
D = numpy.copy(Dat) 
D[:,0] = (1e-9)*D[:,0]
print(D)
Mc = Minimoscuadrados()
[a1,a2,sigma] = Mc.min(D)
x = linspace(min(D[:,0]),max(D[:,0]),100)
g = a1 +a2*x
print(-1/a2)
chi = 0.
for i in range(len(D[:,0])):
    chi += ((D[i,1]-g[i])/sigma[i])**2
print ("distribución chi cuadrada: %0.4f" %(chi))
plt.plot(D[:,0],D[:,1],'bo')
plt.plot(x,g,'b--')
plt.title('Interpolación minimos cuadrados')
plt.ylabel('Numero de particulas Ln(N)')
plt.xlabel('Tiempo')
plt.legend(('Linealizacion de los datos','interpolación'),loc='upper right')
#plt.text(60, 2.7, r'$ \tau $ = %0.4f'%(1/(a2*(-1))), fontsize=10)
