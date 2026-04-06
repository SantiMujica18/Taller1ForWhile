cont = 0 
cont2 = 0
for i in range(6):
    num = float(input("Ingrese las notas: "))
    if num >= 3.6 and num <= 5:
        print("Aprobo")
        cont += 1
    elif num <= 3.5:
        print("no aprobo")
        cont2 += 1
    else:
        print("Coloque un valor valido")
print(f" Aprobaron {cont}")
print(f" No Aprobaron {cont2}")
    