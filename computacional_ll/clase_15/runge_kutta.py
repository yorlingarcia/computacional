from numpy import array, zeros, arange, shape
from math import *
class Runge:
    
    # solucion n dimensional con el cambio de variable en el tiempo
    # u = t/t+1
    def rk4NU(self,h,tint,ro,fun):

        ###########################################################
        # evaluacion de la funcion
        def f(u,r,fun):
            # se define las variables iniciales
            y = zeros(len(r))
            for i in range(len(r)):
                y[i] = r[i]

            # se almacena la evauluacion de la funcion
            # teniendo en cuenta los valores iniciales
            aux = zeros(len(fun))
            for i in range(len(fun)):
                funeval = str(fun[i])
                aux[i] = float(eval(funeval))
            return(aux)
        ##########################################################
        #vector para el cambio de variable del tiempo
        upoints = arange(tint/(1+tint),1,h)
        #vector solucion
        rpoints = []
        # condidiciones iniciales
        r = array(ro,float)
        for u in upoints:
            rpoints.append(list(r))
            k1 = h*f(u,r,fun)
            k2 = h*f(u+0.5*h,r+0.5*k1,fun)
            k3 = h*f(u+0.5*h,r+0.5*k2,fun)
            k4 = h*f(u+h,r+k3,fun)
            # se acutualiza la solucion
            r += (k1+2*k2+2*k3+k4)/6
        return(upoints,rpoints)
#-------------------------------------------------------------------------------#
#-------------------------------------------------------------------------------#
    # solucion n dimensional sin cambio de variable
    def rk4N(self,h,tint,ro,fun):

        ###############################################################
        # evaluacion de la funcion
        def f(t,r,fun):
            # se define la cantidad de variables iniciales
            y = zeros(len(r))
            for i in range(len(r)):
                y[i] = r[i]
            
            # se almacena la evaluacion de la funcion
            # teniendo en cuenta las variables iniciales ya definidas
            aux = zeros(len(fun))
            for i in range(len(fun)):
                funeval = str(fun[i])
                aux[i] = float(eval(funeval))
            return(aux)
        ###############################################################

        tpoints = arange(tint[0],tint[1],h)
        rpoints = []
        r = array(ro,float)
        for t in tpoints:
            rpoints.append(list(r))
            k1 = (h*f(t,r,fun))
            k2 = (h*f(t+0.5*h,r+0.5*k1,fun))
            k3 = (h*f(t+0.5*h,r+0.5*k2,fun))
            k4 = (h*f(t+h,r+k3,fun))
            r += (k1+2*k2+2*k3+k4)/6
        return(tpoints,rpoints)
