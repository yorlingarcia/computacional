from numpy import shape, arange, zeros, array, sqrt, linspace, pi, sin
from scipy.integrate import odeint
from matplotlib import pyplot as plt


# solucion n dimensional sin cambio de variable
def rk4N(h,delta,tint,ro,fun):

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
    
    #tpoints = arange(tint[0],tint[1],h)
    # se define la variable de dominio y rango
    tpoints = []
    rpoints = []
    
    r = array(ro,float)
    rp = array(ro,float)

    # valor inicial
    tpoints.append(tint[0])
    rpoints.append(list(r))
    
    i = 0 # conteo de pasos
    t = tint[0] # tiempo inial acumulativo
    t_temp = 0 # auxiliar para tiempo anterior

    aux_r = array(ro,float)
    aux_rp = array(ro,float)

    while t <= tint[1]:

        true = "on" # variable de validacion de estado
        while true == "on":
            # metodo para el paso h + h
            k1 = (h*f(t,r,fun))
            k2 = (h*f(t+0.5*h,r+0.5*k1,fun))
            k3 = (h*f(t+0.5*h,r+0.5*k2,fun))
            k4 = (h*f(t+h,r+k3,fun))
            aux_r += (k1+2*k2+2*k3+k4)/6
        
            if i == 1: # condicion de dos pasos
                
                hp= 2*h # actualiza el paso
                # metodo para los dos pasos contraidos en uno solo
                # para t = t+h
                k1p = (hp*f(t,r,fun))
                k2p = (hp*f(t+0.5*hp,r+0.5*k1,fun))
                k3p = (hp*f(t+0.5*hp,r+0.5*k2,fun))
                k4p = (hp*f(t+hp,r+k3,fun))
                aux_rp += (k1+2*k2+2*k3+k4)/6

                #rho = 30*h*delta/abs(aux_r[0]-aux_rp[0])
                rho = 30*delta/abs(aux_r[0]-aux_rp[0])
                
                #delta0 = abs(r[0]-rp[0])
                #er = (1/30)*abs((r[0]-rp[0]))
                #aux = delta/er
                
                #if round(aux,1) == delta:
                #    rho = 1
                q = input('pausa = ')
                print("rho = ",rho,"diferencia = ",aux_r[0]-aux_rp[0],"bin = ",h,"tiempo = ",t)
                #print("delta0 = ",delta0,"bin = ",h,"tiempo",t)
                if rho > 0.99 and rho < 1.01:
                    rho = 1
                
                if rho < 1 or rho > 1:
                #if delta0 < delta or delta0 > delta:
                    #h = h*(delta/delta0)**(1/5)
                    h = h*rho**(1/5)
                    i = 0
                    t = t_temp
                    aux_r = r
                    aux_rp = rp
                else :
                    true = "off"
                    i = 0
                    r = aux_r
                    rp = aux_rp

            else :
                t_temp = t
                i += 1
                t += h

        print('salio del ciclo')
        rpoints.append(list(r))
        tpoints.append(t)
    return(tpoints,rpoints)

# parametros
g = 9.8
l = 0.1
delta = 0.1
# realizando el cambio de variables para utilizar el metodo de runge-kutta
# de la clase Runge del metodo rk4N, se tiene
fun = []
fun.append('y[1]')
fun.append('-(9.8/0.1)*sin(y[0])')

# condicion inicial
theta_ini = 179*(pi/180)
theta_pto_ini = 0

ro = [theta_ini, theta_pto_ini] # condicion inicial

h = 0.1 # tamaño del paso(bin)
tt = [0,10] # intervalo temporal
(t,r) = rk4N(h,delta,tt,ro,fun)
print(shape(t),shape(r))
plt.plot(t,r)
plt.show()
