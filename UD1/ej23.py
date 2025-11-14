"""
Dibuja un ordinograma de un programa que lea una secuencia de números no nulos hasta
que se introduzca un 0, y luego muestre si ha leído algún número negativo, cuantos positivos y
cuantos negativos
"""
contador_positivos = 0
contador_negativos = 0
hay_negativo = False
while True:
    print("Introduce un número no nulo (0 para terminar):")
    numero = float(input())
    if numero == 0:
        break
    if numero > 0:
        contador_positivos += 1
    else:
        contador_negativos += 1
        hay_negativo = True
if hay_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")
print("Se han leído", contador_positivos, "números positivos.")
print("Se han leído", contador_negativos, "números negativos.")