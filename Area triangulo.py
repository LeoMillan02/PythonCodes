import math

a=float(input("Inserte lado a: "))
b=float(input("Inserte lado b: "))
c=float(input("Inserte lado c: "))
      
s=(a+b+c)/2
area= math.sqrt(s*(s-a)*(s-b)*(s-c))

print(area)