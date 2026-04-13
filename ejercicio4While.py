import random

randon = random.randint(0,10)

while True:
    ingresar = int(input("Inrese un numero del 0 al 10 para que lo advine: "))
    if randon > ingresar:
        print("El numero es manyor")
    if randon < ingresar:
        print("El numero es menor")
    if randon == ingresar:
        print(f"Adivino el numero es {randon}")
        break