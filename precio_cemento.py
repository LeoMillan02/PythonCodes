#Entradas de datos
cemento=float(input("Inserte la cantidad de costales que se llevara: "))
precio=float(input("Inserte precio del costal: "))

#Operaciones
precio_be= cemento*precio
iva= precio_be*.16
pagar_total= precio_be+iva

print("Precio sin iva:$",precio_be)
print("Iva:$",iva)
print("El total a pagar:$",pagar_total)