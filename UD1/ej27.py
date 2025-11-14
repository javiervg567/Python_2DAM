"""Dibuja un ordinograma de un programa que lea una secuencia de notas (con valores que
van de 0 a 10) que termina con el valor -1 y nos dice si hubo o no alguna nota con valor 10"""
hay_diez = False
while True:
    nota = float(input("Introduce una nota (0-10) o -1 para terminar: "))
    if nota == -1:
        break
    if nota == 10:
        hay_diez = True
if hay_diez:
    print("Se ha leído al menos una nota con valor 10.")
else:
    print("No se ha leído ninguna nota con valor 10.")
    
    