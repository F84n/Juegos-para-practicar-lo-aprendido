"""
programa basico para Una persona que está haciendo una dieta de adelgazamiento necesita saber en los dias que lleva:
-El peso máximo durante ese periodo . 
-El peso mínimo durante ese periodo . 
-El peso medio a lo largo del periodo .
"""

actual=float(input("mete tu peso actual:   "))
N= int(input("dime cuantos dias necesitas calcular?:   "))
contador=0

peso=[]

while contador<N:    # mete los dias que decide el usuario
    contador=contador+1
    c=float(input("mete tu peso por dia:   "))
    peso.append(c)
    
maximo=peso[0]  # calcular el peso maximo
for i in peso:
    for j in peso:
        if i>j and i>maximo:
            maximo=i
print("El peso maximo que has tenido durante estos dias ha sido:   ",maximo, "kg")

minimo=peso[0]   # claculo de peso minimo
for i in peso:
    for j in peso:
        if i < j and i < minimo:
            minimo = i
print("El peso minimo que has tenido ha sido:   ",minimo)

ganado=maximo-actual
perdido=actual-minimo
perdido=round(perdido,2) # solo necesitamos que nos de dos decimales

total=ganado-perdido
print(f"Has ganado {ganado} Kg, y has perdido {perdido} Kg\n En total has ganado o perdido:  {total} Kg")

