import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import csv
import pandas as pd
from scipy import integrate
from scipy import signal

#Se leen los datos y se guarda en la variable "bits" como un int
datos=pd.read_csv("bits10k.csv")
bits = np.array(datos.to_numpy()).astype("int")

"""Se define la cantidad de muestras, la frecuencia, el período,el tamaño N del vector bits, un vector para los puntos 
de muestreo para cada período y la señal sinuidal en la variable sin"""
p=50
f=5000
T=1/f
N =len(bits)
tp = np.linspace(0, T, p)

sin = np.sin(2*np.pi * f * tp)

# Se grafica la función portadora
plt.plot(tp,sin)
plt.xlabel('Tiempo / s')
plt.savefig("portadora.png")
plt.close()



fs = p/T
t = np.linspace(0, N*T, N*p)
senal = np.zeros(t.shape)

for k, b in enumerate(bits):
  if b==1:
    senal[k*p:(k+1)*p] =  sin
  else:
    senal[k*p:(k+1)*p] = -sin

# Visualización de los primeros bits modulados
pb =10
plt.figure()
plt.plot(senal[0:pb*p])
plt.savefig("modulacion.png")
plt.close

#Se gráfica la concatenación
fig, axs = plt.subplots(2)
fig.suptitle('concatenacion')
axs[0].plot(senal[0:pb*p])
axs[1].plot(bits[0:pb+1], drawstyle='steps-pre')
plt.savefig("concatenacion.png")
plt.close

"""Parte 2 Potencia"""
# Se calcula la potencia instananea y la potencia promedio
Pinst = senal**2
Ps = integrate.trapz(Pinst, t) / (N * T)


# Se gráfica la señal antes del canal ruidoso
fw, PSD = signal.welch(senal, fs, nperseg=1024)
plt.figure()
plt.semilogy(fw, PSD)
plt.xlabel('Frecuencia / Hz')
plt.ylabel('Densidad espectral de potencia / V**2/Hz')
plt.savefig("Densidad espectral antes del canal ruidoso")



"""
-En este paso generé un SNR nuevo cada vez que terminaba de graficar la densidad espectral y de calcular el BER 
correspondiente al SNR. Cada valor de BER lo voy guardando en una variable correspondiente donde BER0 pertenece al
SNR=-2, el BER1 a SNR=-1, el BER2 a SNR=0, el BER3 a SNR=1, el BER4 a SNR=2, el BER5 a SNR=3
-El valor Pn es la potencia del ruido para SNR y como se había visto anteriormente Ps es la potencia de la señal. También
se calcula la desviación estándar sigma, el ruido y el canal Rx. Pn,sigma, ruido y Rx cambian de valor para cada valor
de SNR nuevo, por lo que se reescribe cada vez como lo hace el SNR.
-Una vez calculado estos datos se gráfica la densidad espectral correpondiente a cada SNR
-Es importante ver que aquí se están calculando los puntos 3 y 4 en conjunto, y se sobreescribe los valores cada vez que 
empieza un valor nuevo de SNR
-Así al final de cada "ciclo" se calculan los errores correspondientes a la señal con ruido

Para SNR=-2."""
SNR= -2


Pn = Ps / (10**(SNR / 10))
  
  
# Desviación estándar del ruido
sigma = np.sqrt(Pn)


ruido = np.random.normal(0, sigma, senal.shape)


Rx = senal + ruido
  


pb = 5
fw, PSD = signal.welch(Rx, fs, nperseg=1024)

fig, axs = plt.subplots(2)
axs[0].plot(Rx[0:pb*p])
axs[1].plot(fw, PSD)
plt.savefig("Densidadespectral-2.png")
plt.close()


Es = np.sum(sin**2)

# Inicialización del vector de bits recibidos
bitsRx = np.zeros(bits.shape)

# Decodificación de la señal por detección de energía
for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER0 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER0))




"""Para SNR=-1"""
SNR= -1

Pn = Ps / (10**(SNR / 10))
  
sigma = np.sqrt(Pn)


ruido = np.random.normal(0, sigma, senal.shape)

Rx = senal + ruido
  


pb = 5
fw, PSD = signal.welch(Rx, fs, nperseg=1024)

fig, axs = plt.subplots(2)
axs[0].plot(Rx[0:pb*p])
axs[1].plot(fw, PSD)
plt.savefig("Densidadespectral-1.png")
plt.close()

Es = np.sum(sin**2)

bitsRx = np.zeros(bits.shape)


for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER1 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER1))

"""Para SNR=0"""
SNR= 0


Pn = Ps / (10**(SNR / 10))
  
  

sigma = np.sqrt(Pn)

ruido = np.random.normal(0, sigma, senal.shape)


Rx = senal + ruido
  

pb = 5
fw, PSD = signal.welch(Rx, fs, nperseg=1024)

fig, axs = plt.subplots(2)
axs[0].plot(Rx[0:pb*p])
axs[1].plot(fw, PSD)
plt.savefig("Densidadespectral0.png")
plt.close()


Es = np.sum(sin**2)


bitsRx = np.zeros(bits.shape)


for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER2 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER2))




"""Para SNR=1"""
SNR= 1


Pn = Ps / (10**(SNR / 10))
  
  

sigma = np.sqrt(Pn)

ruido = np.random.normal(0, sigma, senal.shape)

Rx = senal + ruido
  


pb = 5
fw, PSD = signal.welch(Rx, fs, nperseg=1024)

fig, axs = plt.subplots(2)
axs[0].plot(Rx[0:pb*p])
axs[1].plot(fw, PSD)
plt.savefig("Densidadespectral1.png")
plt.close()


Es = np.sum(sin**2)

# Inicialización del vector de bits recibidos
bitsRx = np.zeros(bits.shape)

for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER3 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER3))

"""Para SNR=2"""
SNR= 2

Pn = Ps / (10**(SNR / 10))
  

sigma = np.sqrt(Pn)


ruido = np.random.normal(0, sigma, senal.shape)


Rx = senal + ruido
  


pb = 5
fw, PSD = signal.welch(Rx, fs, nperseg=1024)

fig, axs = plt.subplots(2)
axs[0].plot(Rx[0:pb*p])
axs[1].plot(fw, PSD)
plt.savefig("Densidadespectral2.png")
plt.close()


Es = np.sum(sin**2)


bitsRx = np.zeros(bits.shape)


for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER4 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER4))




"""Para SNR=3"""
SNR= 3

 
Pn = Ps / (10**(SNR / 10))
  
  

sigma = np.sqrt(Pn)


ruido = np.random.normal(0, sigma, senal.shape)


Rx = senal + ruido
  


pb = 5
fw, PSD = signal.welch(Rx, fs, nperseg=1024)

fig, axs = plt.subplots(2)
axs[0].plot(Rx[0:pb*p])
axs[1].plot(fw, PSD)
plt.savefig("Densidadespectral3.png")
plt.close()

Es = np.sum(sin**2)


bitsRx = np.zeros(bits.shape)


for k, b in enumerate(bits):
    Ep = np.sum(Rx[k*p:(k+1)*p] * sin)
    if Ep > Es/2:
        bitsRx[k] = 1
    else:
        bitsRx[k] = 0

err = np.sum(np.abs(bits - bitsRx))
BER5 = err/N

print("Para SNR=", SNR, "hay  un total de {} errores en {} bits para una tasa de error de {}.".format(err, N, BER5))



"""Punto 5: Gráficas del BER vs SNR
En este paso se define el vector BER con los resultados de BER correspondientes a los 6 resultados obtenidos"""
#Creo el vector BER con los valores de BER correspondientes a cada SNR
BER=[BER0, BER1, BER2, BER3, BER4, BER5]
#Creo un vector de -2 a 3 que sería la representación de SNR
SNR=np.linspace(-2,3,6)

plt.figure()
plt.plot(SNR, BER, "y")
plt.title("BER vs SNR")
plt.xlabel("SNR (dB)")
plt.ylabel("BER")
plt.savefig("BERvsSNR.png")
plt.close