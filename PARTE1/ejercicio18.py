#Escriba un programa que pida un número por teclado y diga si dicho número es múltiplo de 10.
try:
    numero = int(input("Introduce un número: "))
    
    if numero % 10 == 0:
        print(f"El número {numero} es múltiplo de 10.")
    else:
        print(f"El número {numero} no es múltiplo de 10.") 
except ValueError:
    print("Error: Introduce un número válido.")