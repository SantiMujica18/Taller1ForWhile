valor_cuenta = 1000
usu = "santiago"


while True:
    print("Ingrese el usuario para abrir la cuenta")
    ingrese= input("Ingrese el usuario para continuar: ")
    print("ERROR INGRESE EL USUARIO CORRECTO")
    while ingrese == usu:
        print(f"""
Ingrese lo que desee hacer como operacion:
        "1. Depositar" 
        "2. Retrar"  
        "0.Cerrar Cuenta"
         Su valor es:    {valor_cuenta}
            """)
        pedir = int(input("Igrese lo que desee hacer: "))
        
        if pedir == 1:
            print("Cuanto desea depositar en la cuenta???")
            num = int(input("Ingrese el valor a depositar: "))
            valor_cuenta =  num + valor_cuenta
            print(f" su valor ingresado es {num} y el total es : {valor_cuenta}")
        if pedir == 2:
            print(f"Su saldo en la cuenta es: {valor_cuenta}")
            retiro = int(input("Que valor desea retirar: "))
            if valor_cuenta > retiro:
                valor_cuenta = valor_cuenta - retiro
                print(f"Su retiro fue exitoso le quedan: {valor_cuenta}")
            else:
                print(f"No se puede realizar la solcitud, su valor es {retiro} y tiene {valor_cuenta}")

        if pedir == 0:
            print("CERRAR SESION EXITOSAMENTE")
            break
