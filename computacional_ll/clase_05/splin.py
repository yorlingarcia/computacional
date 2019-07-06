from scipy import linspace
from scipy.interpolate import interp1d
from numpy import loadtxt
import matplotlib.pyplot as plt

a = loadtxt("datafile.dat")
x = linspace(min(a[:,0]),max(a[:,0]),1000)
y = interp1d(a[:,0],a[:,1],kind=('cubic'))(x)

plt.plot(a[:,0],a[:,1],'bo')
plt.plot(x,y,'r')
plt.show()
