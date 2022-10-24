def precio_sin(silla, compra) :
    if silla == "b":
        return compra *700
    elif silla == "e":
        return compra *900
    else:
        return compra *1500

silla=input("Tipo de silla: ")
cliente= input("Tipo de cliente :")
compra= int(input("Numero de sillas :"))


if silla != "b" and silla != "e" and silla != "l":
    print("Silla no valida")
elif cliente != "n" and cliente != "f":
    print("Cliente invalido")
else:
    precio_sin = precio_sin(silla, compra)
    
if cliente == "f":       
    if precio_sin >= 10000 and precio_sin <20000:
        precio_sin *= .90
        print(precio_sin)
    elif precio_sin >= 20000:
        precio_sin *= .85
    else:
        print(precio_sin)
    
else:
    print(precio_sin)
        