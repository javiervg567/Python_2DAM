#Dibuja un ordinograma de un programa que lea 100 números no nulos y luego muestre un mensaje de si ha leído número negativo o no.
hay_negativo = False
for i in range(2):
    print("Introduce un número no nulo:")
    i = float(input())
    if i < 0:
        hay_negativo = True
if hay_negativo:
    print("Se ha leído al menos un número negativo.")
else:
    print("No se ha leído ningún número negativo.")
    