# Método de Gauss-Jordan
# Solución a Sistemas de Ecuaciones
# de la forma A.X=B

import numpy as np
from fileinput import filename



# INGRESO
#nF== Numero de Filas 
nF = int(input('Escribe numero de filas: '))
#nC == Numero de columnas 
nC = int(input('Escribe numero de columnas: '))
matriz=[]
for num_reng in range(nF):
  renglon=[]
  for i in range(nC):
    dato=int(input(f"valor de {num_reng+1},{i+1}: "))
    renglon.append(dato)
  matriz.append(renglon)
matriz2=np.array(matriz,dtype = int)

colRes = []
for i in range (nF):
  fila=[]
  for i in range (1): 
    #valor_in== valor ingresado 
    valor_in= int(input(f"valor {i+1}: "))
    fila.append(valor_in)
  colRes.append(valor_in)

casicero = 1e-15 # Considerar como 0

colRes2=np.array(fila, dtype=float)


#Matriz aumentada
#((matriz,colRes2), axis = 1)
matriz_aumentada = np.concatenate([matriz,colRes2])
matrizAument0 =np.copy (matriz_aumentada)

  
# Pivoteo parcial por filas
size = np.shape(matriz_aumentada)
n = size[0]
m = size[1]
  
# Para cada fila en Matriz aunmentada ¿
for i in range(0,n-1,1):
# columna desde diagonal i en adelante
  columna = abs(matriz_aumentada[i:,i])
  dondemax = np.argmax(columna)
      
# dondemax no está en diagonal
  if (dondemax !=0):
# intercambia filas
    temporal = np.copy(matriz_aumentada[i,:])
    matriz_aumentada[i,:] = matriz_aumentada[dondemax+i,:]
    matriz_aumentada[dondemax+i,:] = temporal
          
  matrizAument1 = np.copy(matriz_aumentada)
  
  # eliminacion hacia adelante
  for i in range(0,n-1,1):
      pivote = matriz_aumentada[i,i]
      adelante = i + 1
      for k in range(adelante,n,1):
          factor = matriz_aumentada[k,i]/pivote
          matriz_aumentada[k,:] = matriz_aumentada[k,:] - matriz_aumentada[i,:]*factor
  matrizAumenta2 = np.copy(matriz_aumentada)
  
  # elimina hacia atras
  ultfila = n-1
  ultcolumna = m-1
  for i in range(ultfila,0-1,-1):
      pivote = matriz_aumentada[i,i]
      atras = i-1 
      for k in range(atras,0-1,-1):
          factor = matriz_aumentada[k,i]/pivote
          matriz_aumentada[k,:] = matriz_aumentada[k,:] - matriz_aumentada[i,:]*factor
      # diagonal a unos
      matriz_aumentada[i,:] = matriz_aumentada[i,:]/matriz_aumentada[i,i]
  X = np.copy(matriz_aumentada[:,ultcolumna])
  X = np.transpose([X])
  
  
  # SALIDA
  print('Matriz aumentada:')
  print(matrizAument0)
  print('Pivoteo parcial por filas')
  print(matrizAument1)
  print('eliminacion hacia adelante')
  print(matrizAumenta2)
  print('eliminación hacia atrás')
  print(matriz_aumentada)
  print('solución de X: ')
  print(X)


