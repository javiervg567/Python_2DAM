# Escriba un programa que lea dos números, calcule y muestre el valor de su suma,
# resta,producto y división (Ten en cuenta la división por cero).
try:
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))
except ValueError:
    print("Entrada no válida. Introduce números.")
else:
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Producto: {a * b}")
    if b != 0:
        print(f"División: {a / b}")
    else:
        print("División: error (no se puede dividir por cero)")
