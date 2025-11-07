#Escriba un programa que simule un cajero automático con un saldo inicial de 1000 dólares,
#con el siguiente menú de opciones:
#Bienvenido a su Cajero Virtual
#1. Ingresar dinero en cuenta
#2. Retirar dinero de la cuenta
#3. Salir
saldo = 1000.0
try:
    while True:
        print("\nBienvenido a su Cajero Virtual")
        print("1. Ingresar dinero en cuenta")
        print("2. Retirar dinero de la cuenta")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == '1':
            ingreso = float(input("Ingresa la cantidad a depositar: "))
            if ingreso > 0:
                saldo += ingreso
                print(f"Has ingresado ${ingreso:.2f}. Saldo actual: ${saldo:.2f}")
            else:
                print("La cantidad a ingresar tiene que ser positiva.")
        
        elif opcion == '2':
            retiro = float(input("Introduce la cantidad a retirar: "))
            if 0 < retiro <= saldo:
                saldo -= retiro
                print(f"Has retirado ${retiro:.2f}. Saldo actual: ${saldo:.2f}")
            else:
                print("Fondos insuficientes o cantidad inválida.")
        
        elif opcion == '3':
            print("Gracias por usar el Cajero Virtual.")
            break
        
        else:
            print("Opción no válida. Selecciona una opción del 1 al 3.")
except ValueError:
    print("Entrada no válida. Introduce un número.")