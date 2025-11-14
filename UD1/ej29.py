"""Dibuja un ordinograma de un programa donde el usuario “piensa” un número del 1 al 100
y el ordenador intenta adivinarlo. Es decir, el ordenador irá proponiendo números una y otra
vez hasta adivinarlo (El usuario deberá indicarlo al ordenador si es mayor o menor o igual al
número pensado)."""
minimo = 1
maximo = 100
print("Piensa un número entre 1 y 100 (incluidos) y yo intentaré adivinarlo.")
input("Pulsa Enter cuando estés listo...")
while True:
    adivinanza = (minimo + maximo) // 2
    print("¿Es tu número", adivinanza, "?")
    respuesta = input("Responde con 'mayor', 'menor' o 'igual': ").strip().lower()
    if respuesta == 'igual':
        print("¡He adivinado tu número!")
        break
    elif respuesta == 'mayor':
        minimo = adivinanza + 1
    elif respuesta == 'menor':
        maximo = adivinanza - 1
    else:
        print("Respuesta no válida. Por favor, responde con 'mayor', 'menor' o 'igual'.")
    if minimo > maximo:
        print("Parece que ha habido un error. ¿Estás seguro de tus respuestas?")
        break