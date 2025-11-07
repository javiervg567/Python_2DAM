#Escriba un programa que calcule el área de un cuadrado cuyo lado se introduce por teclado. (El área del cuadrado es igual a lado por lado)
try:
    lado = float(input("Introduce el lado del cuadrado: "))
    if lado < 0:
        print("El lado no puede ser negativo.")
    else:
        area = lado * lado
        print(f"El área del cuadrado es: {area}")
except ValueError:
    print("Entrada no válida. Introduce un número.")
