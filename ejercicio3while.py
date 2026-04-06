cont = 0 
num = 1
while True:
    num = int(input("Ingrese un numero hasta que coloque uno negativo: "))
    if num < 0 :
        break
    cont += 1
print(f" Los numeros ingresados son : {cont}")
