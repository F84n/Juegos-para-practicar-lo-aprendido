""" “Adivina el Número”. La computadora pensará un número aleatorio entre 1 y 20, y te pedirá que 
intentes adivinarlo. La computadora te dirá si cada intento es muy alto o muy bajo. 
Tú ganas si adivinas el número en seis intentos o menos.

"""
print("++++++++++++++__________++++++++++++++")
import random


a=input("Empecemos por saber como te llamas.    ")
print(f" Hola {a} , vamos a jugar a que adivines el numero que estoy pensando del 1 al 20,\n tienes 6 oportunidades para ganarme    ")
numero=int(input("Dime tu primer numero     "))
intentos=0
numero2=0

if numero >22 or numero<=0:
    print("Error, mete otro numero segun los parametros (números de 1 al 20)")
    numero=int(input("numero: "))
       
comienza = random.randint(0, 21)

while numero<21 and numero>0:
          
    if numero>comienza:
        numero= int(input("!!!! Te has pasado !!!!,mete otro numero"))
        intentos=intentos+1
    elif numero<comienza:
        numero=int(input("No has llegado, mete otro numero mas alto"))
        intentos = intentos+1
    elif numero==comienza:
        print("!!! Has acertado, has ganado el juego !!!, los has consegido con  ",intentos, "intentos")
        break
    if intentos>=6:
        print(" !!! Has perdido, te has pasado de numero de intentos !!!")
        break
    



    
    
