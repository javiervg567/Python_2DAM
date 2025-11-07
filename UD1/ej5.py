#Escriba un programa que toma como dato de entrada un número que corresponde a la
#longitud de un radio (La longitud del radio es la mitad de la del diámetro) y nos escribe la longitud
#de la circunferencia (La longitud de una circunferencia es igual a pi por el diámetro), el área del
#círculo (El área de un círculo es pi multiplicado por el radio al cuadrado) y el volumen de la esfera
#que corresponde con dicho radio.
import math
try:
    r = float(input("Introduce la longitud del radio: "))
    if r < 0:
        print("El radio no puede ser negativo.")
    else:
        circunferencia = 2 * math.pi * r
        area = math.pi * r**2
        volumen = 4/3 * math.pi * r**3

        print(f"Longitud de la circunferencia: {circunferencia:.6f}")
        print(f"Área del círculo: {area:.6f}")
        print(f"Volumen de la esfera: {volumen:.6f}")
except ValueError:
    print("Introduce un número.")