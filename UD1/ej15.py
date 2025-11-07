#Escriba un programa que lee dos números y muestra el mayor.
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
if a > b:
    print(f"El mayor es: {a}")
elif b > a:
    print(f"El mayor es: {b}")