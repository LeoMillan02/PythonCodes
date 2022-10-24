"""Gaus Jordan"""
import numpy as np
from fileinput import filename
from numpy import zeros, fabs

def crea_matriz(r,c):
    print(f"matriz {r}*{c}: ")
    matriz=[]
    for num_reng in range(r):
        renglon=[]
        for i in range(c):
            dato=int(input(f"valor de {num_reng+1},{i+1}: "))
            renglon.append(dato)
        matriz.append(renglon)
    matriz2=np.array(matriz,dtype=int)
    return matriz2

def matriz_ind(n):
    b=[]
    for i in range(n):
        renglon=[]
        for i in range(1):
            dato=int(input(f"valor {i+1}: "))
            renglon.append(dato)
        b.append(renglon)
    b2=np.array(b,dtype=float)
    return b2
        
def crear_matrizAumentada(r,c,m,b):
    ma=np.concatenate((m,b),axis=1)
    print(ma)
    return ma

def num_Soluciones(col,r,r2):
    if (r == r2):
        if (r == col):
            print(f"Solución única:")

def gaussJordan(AB,n,m):
    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna = abs(AB[i:,i])
        dondemax = np.argmax(columna)
    
        # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    for i in range(0,n-1,1):
        pivote = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila,0-1,-1):
        pivote = AB[i,i]
        atras = i-1 
        for k in range(atras,0-1,-1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
        # diagonal a unos
        AB[i,:] = AB[i,:]/AB[i,i]
    X = np.copy(AB[:,ultcolumna])
    X = np.transpose([X])
    print(AB)
    return X


"Main"
casicero = 1e-15
ren=int(input("numero de filas: "))
col=int(input("numero de columnas: "))
mat=crea_matriz(ren,col)
b=matriz_ind(ren)

print(" ")
print("MATRIZ")
print(mat)
print(" ")
print("MATRIZ AUMENTADA")
matA=crear_matrizAumentada(ren, col, mat, b)
tamano = np.shape(matA)
n = tamano[0]
m = tamano[1]
print(" ")
print("MATRIZ ESCALONADA")
A=gaussJordan(matA,n,m)
print(A)
rang = np.linalg.matrix_rank(mat) 
rang2 = np.linalg.matrix_rank(matA)


print(" ")
print(f"El rango de la MATRIZ es: {rang}")
print(f"El rango de la Matriz Aumentada es: {rang2}")
print(" ")
