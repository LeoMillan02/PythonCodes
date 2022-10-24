#Actividad 4. Sistemas de ecuaciones lineales
#Método de Gauss-Jordan
#Carlos Antonio Solano Vega - A01540077
#Jorge Carrillo Castro - A01634630
#Leonardo Millán Velázquez - A01639823


import numpy as np
casicero = 1e-15 # Considerar como 0
nF=int(input("Numero de filas: ")) 
nC=int(input("Numero de columnas: ")) 

print(f"matriz {nF}*{nC}: ")
matriz = []
for numFilas in range(nF): 
    fila=[] 
    for i in range(nC):
        valor = int(input(f"Valor de {numFilas+1},{i+1}: "))
        fila.append(valor)
    matriz.append(fila)
matriz2 = np.array(matriz,dtype=float)
mat = matriz2

mat_b = []
for i in range(nF):
    fila = []
    for n in range(1):
        valor = int(input(f"Valor {i+1}: "))
        fila.append(valor)
    mat_b.append(fila)
mat_b2 = np.array(mat_b,dtype = float)

mat_ab = np.concatenate((mat,mat_b),axis=1)
print(mat)
mat_ab0 = np.copy(mat_ab)

# Pivoteo parcial por filas
size = np.shape(mat_ab)
n = size[0]
m = size[1]

# Para cada fila en AB
for i in range(0,n-1,1):
    # columna desde diagonal i en adelante
    columna = abs(mat_ab[i:,i])
    dondemax = np.argmax(columna)
    
    # dondemax no está en diagonal
    if (dondemax !=0):
        # intercambia filas
        temp = np.copy(mat_ab[i,:]) #temporal
        mat_ab[i,:] = mat_ab[dondemax+i,:]
        mat_ab[dondemax+i,:] = temp
        
ab_1 = np.copy(mat_ab)

# eliminacion hacia adelante
for i in range(0,n-1,1):
    pivote = mat_ab[i,i]
    adelante = i + 1
    for k in range(adelante,n,1):
        factor = mat_ab[k,i]/pivote
        mat_ab[k,:] = mat_ab[k,:] - mat_ab[i,:]*factor
ab_2 = np.copy(mat_ab)

# elimina hacia atras
ultfila = n-1
ultcolumna = m-1
for i in range(ultfila,0-1,-1):
    pivote = mat_ab[i,i]
    atras = i-1 
    for k in range(atras,0-1,-1):
        factor = mat_ab[k,i]/pivote
        mat_ab[k,:] = mat_ab[k,:] - mat_ab[i,:]*factor
    # diagonal a unos
    mat_ab[i,:] = mat_ab[i,:]/mat_ab[i,i]
x = np.copy(mat_ab[:,ultcolumna])
x = np.transpose([x])

rango = np.linalg.matrix_rank(mat) 
rango2 = np.linalg.matrix_rank(mat_ab)

# SALIDA
print('Matriz aumentada:')
print(mat_ab0)
print('Eliminación hacia atrás')
print(mat_ab)
print('Solución de X: ')
print(x)
print(" ")
print(f"El rango de la MATRIZ es: {rango}")
print(f"El rango de la Matriz Aumentada es: {rango2}")
print(" ")
