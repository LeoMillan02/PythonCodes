palabras = []
palabra = input()
contador= 0

while len(palabra) > 1:
    
    palabras.append(palabra)
    palabra = input()

for i in palabras:
    if i[0].upper() == palabra.upper():
        contador += 1
        
print(contador)
    
