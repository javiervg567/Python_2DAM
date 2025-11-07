#Escriba un programa que lea tres números y nos diga cual es mayor, cual menor y cuales
#son iguales.
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    
    if num1 >= num2 and num1 >= num3:
        mayor = num1
    elif num2 >= num1 and num2 >= num3:
        mayor = num2
    else:
        mayor = num3
        
    if num1 <= num2 and num1 <= num3:
        menor = num1
    elif num2 <= num1 and num2 <= num3:
        menor = num2
    else:
        menor = num3
    
    print(f"\nRESULTADOS:")
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")
    
    igualdades = []
    if num1 == num2:
        igualdades.append(f"Primero y Segundo ({num1})")
    if num1 == num3:
        igualdades.append(f"Primero y Tercero ({num1})")
    if num2 == num3:
        igualdades.append(f"Segundo y Tercero ({num2})")
    
    if num1 == num2 == num3:
        print("Los tres números son iguales")
    elif igualdades:
        print("Números iguales:", ", ".join(igualdades))
    else:
        print("No hay números iguales")
        
except ValueError:
    print("Error: Por favor ingrese números válidos")