#Escriba un programa que lea dos números y lo visualiza en orden ascendente.
try:
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
except ValueError:
    print("Introduce números.")
else:
    if a <= b:
        print("Orden ascendente:", a, b)
    else:
        print("Orden ascendente:", b, a)