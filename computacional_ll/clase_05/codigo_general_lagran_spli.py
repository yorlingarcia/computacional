import matplotlib.pyplot as pl
from numpy import loadtxt
from scipy.interpolate import interp1d
from scipy import linspace

class lagrange:
    def __init__(self):
        print("Clase inicializada")
    
    def interpolacion(self,xm,ym, x_interp):
        n = len(xm)
        y_interp = []
        for x in range(len(x_interp)):
            y = 0.
            for j in range(len(ym)):
                ele = 1.
                m = 0
                while m < n:
                    if m != j:
                        ele *=(x_interp[x]-xm[m])/(xm[j]-xm[m]) 
                    m += 1
                y += ele*ym[j]
            y_interp.append(y)
        return (y_interp)
    
    
a = loadtxt("datafile.dat")
#fig = pl.figure(figsize= (4,4), dpi=100)
#pl.scatter(a[:,0],a[:,1])
#pl.title("Datos Experimentales")
#pl.xlabel("E")
#pl.ylabel("F(e)")
#pl.grid("on")

rango_interp = linspace(min(a[:,0]),max(a[:,0]),100)

y = interp1d(a[:,0],a[:,1],kind=('cubic'))(rango_interp)

interpo = lagrange()
fun = interpo.interpolacion(a[:,0],a[:,1],rango_interp)
pl.plot(rango_interp,y)
pl.scatter(a[:,0],a[:,1])
pl.plot(rango_interp,fun)