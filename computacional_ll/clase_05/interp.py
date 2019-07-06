from numpy import loadtxt
import matplotlib.pyplot as plt
from lagrange import Lagrange
from scipy import linspace
from scipy.interpolate import interp1d

a = loadtxt("datafile.dat")

xinterp = linspace(min(a[:,0]),max(a[:,0]),100)

Lg = Lagrange()
punt = Lg.funcion(a[:,0], a[:,1], xinterp)
y = interp1d(a[:,0],a[:,1],kind=('cubic'))(xinterp)
plt.plot(xinterp,y,'k')
plt.plot(a[:,0],a[:,1],'bo') 
plt.plot(xinterp,punt)
plt.show()

