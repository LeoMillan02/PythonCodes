#####################
#Función de transferencia
############################
#Instalación de librerias
############################
import numpy as np

import control

from scipy import signal

import matplotlib.pyplot as plt

#################################
Kp = 5
Ti = 2
Td = 15
##################################
#Opción 1
Numerador = np.array([Kp*Td*Ti, Kp*Ti, Kp])
Denominador = np.array([Ti, Kp*Td*Ti, Ti+Kp*Ti, Kp])
#T = control.tf(Numerador, Denominador)

######################################################

#Opción 2
s = control.TransferFunction.s
T = (Kp*Td*Ti*s**2+Kp*Ti*s)/(Ti*s**3+(Kp*Td*Ti)*s**2+(Ti+Kp*Ti)*s+Kp)
print('T(s) = ',T)
#############################################################################
#Repuesta del Sistema en lazo cerrado
#Entrada de referencia escalón unitario
lti = signal.lti(Numerador, Denominador)
t,y = signal.step(lti)
#Graficación de la Respuesta del sistema
plt.plot(t,y)
plt.title("Respuesta al escalón")
plt.xlabel("Tiempo")
plt.ylabel("x(t)")
plt.grid()
plt.show()
##############################################################################