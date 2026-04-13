contador = 1

num = int(input("Ingrese el numero que desee realizar la tabla de multiplicar: "))
while contador <= 10:
    result = num * contador
    print(f" {contador} * {num} = {result}")
    contador += 1