import numpy as np
from momento import Momento
#tener en cuenta que no acepta caracteres no ingleses
mu=5
sg=1
nevents=10000
#crea una dsitribucion aleatoria normal
s=np.random.normal(mu, sg, nevents)
#crea una archivo .dat con permiso de escritura
outDisdat1 = open("datafiles_01.dat","w")
###############################################
#guardar los datos en el erchivo .dat
for i in range(len(s)):
    outDisdat1.write('%d\n' % (s[i]))
outDisdat1.close()
###############################################
#crear un histograma
hist = []  # crea un vector de tamano indefinido
startbin=0.
endbin=10.
nbins=100
binwidth=(endbin - startbin)/nbins
[hist.append(0) for i in range(nbins)] # agrega un cero a cada posicion del vector

# podemos construir un histograma de los datos de dat
# sin utilizar codigo condicionado
# utilizando la posicion del vector hist[], es posible hacer un conteo(frecuencial) de los datos dat
# utilizando un ciclo

for i in s:
    hist[ int(i/binwidth) ] += 1
#iniciamos un archivo para guardar la frecuencia hist y la clase(eje x [startbin endbin])
outDisdat = open("datafile.dat","w")
outDisdat.write("# startbin %0.1f endbin %0.1f nbins %d\n" % (startbin, endbin, nbins))
# cada ves que se escribe sobre un archivo este  se inicia sobre la siguiente linea
for j in range(nbins):
    outDisdat.write('%0.4f  %d\n' % (j*binwidth ,hist[j]))
outDisdat.close()

############################################################
inData = open("datafile.dat","r")
mt = Momento()
[media, N] = mt.momento1(inData)
#inData = open("datafile.dat","r")
sigma = mt.momento2(media, N)
mt.momento3(media, N, sigma)
mt.momento4(media, N, sigma)
