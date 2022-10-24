
n= int(input())
di= 1
div=0

while di < n:
    if n% di == 0:
         div = div +di
    di += 1
if div == n:
    print("perfecto")
else:
    print("imperfecto")
    
 