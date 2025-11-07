#Escriba un programa que lea dos números y nos diga cual es mayor o si son iguales.
a = float(input("Introduce el primer número: "))
b = float(input("Introduce el segundo número: "))
if a > b:
    print(f"El mayor es: {a}")
elif b > a:
    print(f"El mayor es: {b}")
else:
    print("Los números son iguales")